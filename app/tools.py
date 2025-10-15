# Importing Required Modules/Libraries

import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.tools import Tool
from langchain_experimental.utilities import PythonREPL
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# loading API Key's from .env using dotenv
load_dotenv()

# TOOL 1 - Tavily Tool

def get_tavily_tool():
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("Tavily API Key not found.")
    return TavilySearchResults(api_key=api_key)

# TOOL 2 - Wikipedia Tool

def get_wikipedia_tool():
    wrapper =WikipediaAPIWrapper()
    return WikipediaQueryRun(api_wrapper=wrapper)

# TOOL 3 - Calculator Tool using PythonREPLTool

def get_calculator_tool():
    repl = PythonREPL()
    return Tool(
        name="Calculator",
        func=repl.run,
        description="Useful for evaluating math expressions using Python syntax."
    )


# TOOL 4 - Custom PDF Q&A Tool

def get_pdf_qa_tool(pdf_path:str,local_llm):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File was not Found at path : {pdf_path}")
    loader = PyPDFLoader(pdf_path)
    documents=loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0
    )
    chunks = splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks,embeddings)
    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm = local_llm,
        retriever = retriever,
        return_source_documents = True
    )

    def pdf_tool_fn(query: str):
        print(f"[PDF TOOL DEBUG] Received query: {query}")
        result = qa_chain.invoke({"query": query})
        print(f"[PDF TOOL DEBUG] Full result: {result}")
        return result

    return Tool(
        name="PDF_QA_Tool",
        func=pdf_tool_fn,
        description="This is the ONLY way to access PDF content. ALWAYS use this tool to answer any question"
    )
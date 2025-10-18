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

load_dotenv()


def get_tavily_tool():
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("Tavily API Key not found.")
    return TavilySearchResults(api_key=api_key)


def get_wikipedia_tool():
    wrapper = WikipediaAPIWrapper()
    return WikipediaQueryRun(api_wrapper=wrapper)


def get_calculator_tool():
    repl = PythonREPL()
    return Tool(
        name="Calculator",
        func=repl.run,
        description="Useful for evaluating math expressions using Python syntax."
    )


def get_pdf_qa_tool(pdf_path: str, local_llm):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    qa_chain = RetrievalQA.from_chain_type(
        llm=local_llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )

    def pdf_tool_fn(query: str) -> str:
        result = qa_chain.invoke({"query": query})
        if isinstance(result, dict):
            return str(result.get('result', ''))
        return str(result)

    return Tool(
        name="PDF_QA",
        func=pdf_tool_fn,
        description="Query the uploaded PDF document. Input should be a specific question like 'What is the project goal?' or 'What datasets are mentioned?'. The PDF is already loaded."
    )
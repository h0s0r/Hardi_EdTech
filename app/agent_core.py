from platform import system
from tabnanny import verbose

from langchain.agents import initialize_agent,AgentType
from langchain_community.llms import Ollama
from langchain_ollama import ChatOllama
import os

from app.tools import (
    get_tavily_tool,
    get_wikipedia_tool,
    get_calculator_tool,
    get_pdf_qa_tool
)

def get_local_llm():
    return ChatOllama(model="gpt-oss:20b")

def get_default_tools():
    return [
        get_calculator_tool(),
        get_wikipedia_tool(),
        get_tavily_tool()
    ]

def create_agent_executor(pdf_path: str = None):
    llm = get_local_llm()
    tools = get_default_tools()

    if pdf_path and os.path.isfile(pdf_path) and pdf_path.lower().endswith(".pdf"):
        pdf_tool = get_pdf_qa_tool(pdf_path=pdf_path, local_llm=llm)
        tools.append(pdf_tool)

    agent_executor = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations= 10
    )
    return agent_executor
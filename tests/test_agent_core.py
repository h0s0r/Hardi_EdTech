import os, tempfile, shutil
from app.agent_core import create_agent_executor
from langchain.agents.agent import AgentExecutor

def test_agent_no_pdf():
    print('\n Agent Test without pdf has Started.')
    agent = create_agent_executor()
    assert isinstance(agent,AgentExecutor)
    assert len(agent.tools) >= 3
    tool_names = [tool.name for tool in agent.tools]
    assert "tavily_search_results_json" in tool_names
    assert "wikipedia" in tool_names
    assert "Calculator" in tool_names
    print(f"\nTools available - {tool_names}")

def test_agent_pdf():
    agent = create_agent_executor(pdf_path="/home/h0s0r/PROJECTS/Hardi_EdTech/tests/CustomPdfQAToolTestQuerySample.pdf")
    tool_names = [tool.name for tool in agent.tools]
    assert "PDF_QA_Tool" in tool_names

def test_agent_response():
    print("Agent Starting Up!!")
    print("Agent Executor Starting!!!")
    agent = create_agent_executor(pdf_path="/home/h0s0r/PROJECTS/Hardi_EdTech/tests/CustomPdfQAToolTestQuerySample.pdf")
    print("Agent Executor Created!\nInvoking the Agent Now!!!")
    response = agent.invoke(
        {
            "input": "Hi, Who are you?",
            "chat_history": []
        },
    )
    print("Invoking was successful Now the Response is coming up.")
    print(response["output"])
    output_text = response["output"]
    assert isinstance(output_text, str)
    # assert output_text.lower().startswith("hi")
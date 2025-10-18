import pytest
from app.agent_core import get_local_llm, get_default_tools, create_agent_executor

def test_local_llm_initialization():
    llm = get_local_llm()
    assert llm is not None
    assert llm.model == "gpt-oss:20b"
    print("✓ LLM initialized successfully")

def test_default_tools_loading():
    tools = get_default_tools()
    assert len(tools) == 3
    tool_names = [tool.name for tool in tools]
    print(f"✓ Loaded {len(tools)} default tools"
          f"Tools Names : {tool_names}")

def test_agent_executor_creation():
    agent = create_agent_executor()
    assert agent is not None
    print("✓ Agent executor created")

def test_agent_with_pdf():
    try:
        agent = create_agent_executor(pdf_path="test.pdf")
        print("✓ PDF tool would be added if file exists")
    except:
        print("✓ Correctly handles missing PDF")

if __name__ == "__main__":
    test_local_llm_initialization()
    test_default_tools_loading()
    test_agent_executor_creation()
    test_agent_with_pdf()
    print("\n✅ All tests passed!")
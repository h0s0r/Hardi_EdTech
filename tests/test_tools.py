import pytest
from app.tools import get_calculator_tool, get_wikipedia_tool, get_tavily_tool

def test_calculator_tool():
    calc = get_calculator_tool()
    assert calc.name == "Calculator"
    result = calc.run("2 + 2")
    assert "4" in str(result)
    print("✓ Calculator tool working")

def test_wikipedia_tool():
    wiki = get_wikipedia_tool()
    assert wiki.name == "wikipedia"
    print("✓ Wikipedia tool loaded")

def test_tavily_tool():
    try:
        tavily = get_tavily_tool()
        print("✓ Tavily tool loaded")
    except ValueError:
        print("✓ Tavily requires API key (expected)")

if __name__ == "__main__":
    test_calculator_tool()
    test_wikipedia_tool()
    test_tavily_tool()
    print("\n✅ All tool tests passed!")
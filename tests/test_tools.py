from app.tools import get_tavily_tool, get_wikipedia_tool, get_calculator_tool, get_pdf_qa_tool
from langchain_community.llms import Ollama

def test_tavily_1():

    print("\nRunning Test for Tavily Search Tool")
    tavily_tool = get_tavily_tool()
    # Running a Sample - query_1
    query_1 = "Latest Real Time News about AI"
    result_1 = tavily_tool.run(query_1)
    print("\n Tavily Search Result")
    print(result_1)

def test_wikipedia():
    print("\nRunning Test for Wikipedia Tool")
    wiki_tool = get_wikipedia_tool()
    query_2 = "Python"
    result_2 =wiki_tool.run(query_2)
    print(result_2)

def test_calculator():
    print("\nRunning Test for Calculator Tool (Python REPL based)")
    calculator = get_calculator_tool()
    query_3 = "25 * (4 + 3)"
    result_3 = calculator.run(query_3)
    print("\nCalculator Result:")
    print(result_3)


def test_pdf_qa():
    print("\nRunning test for Custom PDF QA Tool")
    pdf_path = "/home/h0s0r/PROJECTS/Hardi_EdTech/tests/CustomPdfQAToolTestQuerySample.pdf"
    query_4 = "Share all the info you have about AI in personalised Learning."
    local_llm = Ollama(model="gpt-oss:20b")
    qa_tool = get_pdf_qa_tool(pdf_path, local_llm)

    result_dict = qa_tool.func(query_4)  # use .func instead of .run
    print("\n📘 Answer:")
    print(result_dict["result"])

if __name__ == "__main__":
    test_tavily_1()
    test_wikipedia()
    test_calculator()
    test_pdf_qa()
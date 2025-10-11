from app.tools import get_tavily_tool

def test_tavily_1():

    print("Running Test for Tavily Search Tool")
    tavily_tool = get_tavily_tool()

    # Running a Sample - query_1
    query_1 = "Latest Worldwide news about Artificial Intelligence."
    result_1 = tavily_tool.run(query_1)

    print("\n Tavily Search Result")
    print(result_1)

if __name__ == "__main__":
    test_tavily_1()
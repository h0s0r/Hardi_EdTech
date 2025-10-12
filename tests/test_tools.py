from app.tools import get_tavily_tool, get_wikipedia_tool

def test_tavily_1():

    print("\nRunning Test for Tavily Search Tool")
    tavily_tool = get_tavily_tool()
    # Running a Sample - query_1
    query_1 = input("Enter a Query for Tavily(Real Time Web Result) Checkup - ")
    result_1 = tavily_tool.run(query_1)
    print("\n Tavily Search Result")
    print(result_1)

def test_wikipedia():
    print("\nRunning Test for Wikipedia Tool")
    wiki_tool = get_wikipedia_tool()
    query_2 = input("Enter a Query for Wikipedia(searches Wikipedia for info related to the query) Checkup - ")
    result_1 =wiki_tool.run(query_2)
    print(result_1)

if __name__ == "__main__":
    # test_tavily_1()
    test_wikipedia()
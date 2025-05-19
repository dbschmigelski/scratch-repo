from mcp.server import FastMCP


def start_server():
    mcp = FastMCP("Echo Server")

    @mcp.tool(description="Returns the day of the week")
    def what_day_is_it() -> str:
        return "Monday"

    mcp.run(transport="stdio")


if __name__ == "__main__":
    start_server()

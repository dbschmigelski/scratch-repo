from mcp import stdio_client, StdioServerParameters
import asyncio

async def start_server():
  client = stdio_client(StdioServerParameters(command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"]))

  async with client as (read_stream, write_stream):
    async with ClientSession(read_stream, write_stream) as session:
        await session.initialize()
        print("INITIALIZED")

if __name__ == "__main__":
    asyncio.run(start_server())

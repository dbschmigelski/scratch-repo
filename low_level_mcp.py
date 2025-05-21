from mcp import ClientSession, stdio_client, StdioServerParameters
import asyncio

async def start_server():
  client = stdio_client(StdioServerParameters(command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"]))

  async with client as (read_stream, write_stream):
    async with ClientSession(read_stream, write_stream) as session:
        await session.initialize()
        print("INITIALIZED")
        print(await session.list_tools())

if __name__ == "__main__":
    asyncio.run(start_server())

from mcp import stdio_client, StdioServerParameters
import asyncio

async def start_server():
  client = stdio_client(StdioServerParameters(command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"]))

  async with client:
    await client.initialize()
    print("INITIALIZED")

if __name__ == "__main__":
    asyncio.run(start_server())

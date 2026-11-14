import asyncio
from mcp import Client


async def main():
    async with Client("http://localhost:8000/mcp") as client:

        tools = await client.list_tools()

        print([tool.name for tool in tools.tools])

        result = await client.call_tool(
            "get_total_expense",
            {"category": "Food"}
            
        )

        print(result.structured_content)


if __name__ == "__main__":
    asyncio.run(main())
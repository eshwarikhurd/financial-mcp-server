import asyncio
import os
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types
from dotenv import load_dotenv

from tools.financials import get_company_financials
from tools.peers import compare_peers
from tools.summarize import summarize_10k

load_dotenv()

app = Server("financial-mcp-server")

@app.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="get_company_financials",
            description="Get key financial metrics for a company including revenue, net income, margins and EPS",
            inputSchema={
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "Stock ticker symbol e.g. AAPL, MSFT, GOOGL"
                    }
                },
                "required": ["ticker"]
            }
        ),
        types.Tool(
            name="compare_peers",
            description="Compare financial metrics of a company against its peers",
            inputSchema={
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "Main company ticker symbol"
                    },
                    "peers": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of peer ticker symbols to compare against"
                    }
                },
                "required": ["ticker", "peers"]
            }
        ),
        types.Tool(
            name="summarize_10k",
            description="Fetch and summarize the latest 10-K annual filing for a company with source citations",
            inputSchema={
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "Stock ticker symbol"
                    }
                },
                "required": ["ticker"]
            }
        ),
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "get_company_financials":
        result = await get_company_financials(arguments["ticker"])
        return [types.TextContent(type="text", text=str(result))]

    elif name == "compare_peers":
        result = await compare_peers(arguments["ticker"], arguments["peers"])
        return [types.TextContent(type="text", text=str(result))]

    elif name == "summarize_10k":
        result = await summarize_10k(arguments["ticker"])
        return [types.TextContent(type="text", text=str(result))]

    else:
        raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
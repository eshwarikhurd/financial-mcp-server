# Financial MCP Server 💹

An MCP (Model Context Protocol) server that gives Claude real-time financial intelligence tools — built as a mini version of what [Genios AI](https://geniosai.co) does at scale.

## Tools

| Tool | Description |
|---|---|
| `get_company_financials` | Fetches revenue, net income, margins, EPS for any public company |
| `compare_peers` | Side-by-side financial comparison of a company vs its peers |
| `summarize_10k` | Fetches latest 10-K from SEC EDGAR and summarizes it with source citations using Claude |

## Demo

> "Compare AAPL with MSFT and GOOGL"

Claude automatically calls `compare_peers("AAPL", ["MSFT", "GOOGL"])` and returns a structured comparison table with live data.

> "Summarize the 10-K for MSFT"

Claude fetches the actual SEC filing and returns a cited summary broken down by Business Overview, Financial Highlights, Risk Factors, and Management Outlook.

## Tech Stack

- **MCP SDK** — Anthropic's Model Context Protocol for tool definitions
- **Financial Modeling Prep API** — real-time financial data
- **SEC EDGAR API** — official 10-K filings
- **Anthropic Claude API** — summarization with source citations
- **httpx** — async HTTP requests
- **pydantic** — structured data validation

## Setup

1. Clone the repo
2. Create a virtual environment and install dependencies:
```bash
   python -m venv venv
   source venv/bin/activate
   pip install mcp httpx pydantic python-dotenv anthropic
```
3. Create a `.env` file:
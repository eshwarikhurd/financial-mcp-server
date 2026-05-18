# Financial MCP Server 💹

An MCP (Model Context Protocol) server that gives Claude real-time financial intelligence tools — built as a mini version of what [Genios AI](https://geniosai.co) does at scale.

## Tools

| Tool | Description |
|---|---|
| `get_company_financials` | Fetches revenue, net income, margins, EPS for any public company |
| `compare_peers` | Side-by-side financial comparison of a company vs its peers |
| `summarize_10k` | Fetches latest 10-K from SEC EDGAR and summarizes it with source citations using Claude |


## Demo

### 📊 Get Company Financials
> "Get me the financials for AAPL"

![Financials 1](outputs/financials_1.png)
![Financials 2](outputs/financials_2.png)

### 🔍 Compare Peers
> "Compare AAPL with MSFT and GOOGL"

![Peers 1](outputs/peers_1.png)
![Peers 2](outputs/peers_2.png)

### 📄 Summarize 10-K
> "Summarize the 10-K for AAPL"

![Summarize 1](outputs/summarize_1.png)
![Summarize 2](outputs/summarize_2.png)

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
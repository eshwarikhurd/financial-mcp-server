import httpx
import os
import asyncio
from dotenv import load_dotenv
from tools.financials import get_company_financials


load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
BASE_URL = "https://financialmodelingprep.com/api/v3"

async def compare_peers(ticker: str, peers: list[str]) -> dict:
    """Compare financials of a company against its peers."""
    all_tickers = [ticker] + peers
    results = []


    results = await asyncio.gather(
        *[get_company_financials(t) for t in all_tickers]
    )
    results = list(results)

    # Build comparison table
    comparison = {
        "companies": [],
        "metrics": ["revenue", "net_income", "gross_margin", "net_margin", "eps", "market_cap"]
    }

    for company in results:
        if "error" not in company:
            comparison["companies"].append({
                "ticker": company["ticker"],
                "company_name": company["company_name"],
                "revenue": company["revenue"],
                "net_income": company["net_income"],
                "gross_margin": company["gross_margin"],
                "net_margin": company["net_margin"],
                "eps": company["eps"],
                "market_cap": company["market_cap"],
                "period": company["period"],
            })

    return comparison
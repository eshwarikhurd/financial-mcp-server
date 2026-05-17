import httpx
import os
from dotenv import load_dotenv

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
BASE_URL = "https://financialmodelingprep.com/api/v3"

async def get_company_financials(ticker: str) -> dict:
    """Fetch key financial metrics for a company."""
    async with httpx.AsyncClient() as client:
        # Get income statement
        income_url = f"{BASE_URL}/income-statement/{ticker}?limit=1&apikey={FMP_API_KEY}"
        profile_url = f"{BASE_URL}/profile/{ticker}?apikey={FMP_API_KEY}"

        income_res = await client.get(income_url)
        profile_res = await client.get(profile_url)

        income_data = income_res.json()
        profile_data = profile_res.json()

        if not income_data or not profile_data:
            return {"error": f"No data found for ticker {ticker}"}

        income = income_data[0]
        profile = profile_data[0]

        return {
            "ticker": ticker,
            "company_name": profile.get("companyName"),
            "sector": profile.get("sector"),
            "market_cap": profile.get("mktCap"),
            "revenue": income.get("revenue"),
            "net_income": income.get("netIncome"),
            "gross_profit": income.get("grossProfit"),
            "operating_income": income.get("operatingIncome"),
            "eps": income.get("eps"),
            "gross_margin": round(income.get("grossProfit", 0) / income.get("revenue", 1) * 100, 2),
            "net_margin": round(income.get("netIncome", 0) / income.get("revenue", 1) * 100, 2),
            "period": income.get("date"),
        }
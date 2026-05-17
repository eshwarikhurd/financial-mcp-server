import httpx
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
BASE_URL = "https://financialmodelingprep.com/api/v3"
client = Anthropic()

async def summarize_10k(ticker: str) -> dict:
    """Fetch and summarize the latest 10-K filing for a company."""
    async with httpx.AsyncClient() as http_client:
        # Get SEC filings
        filings_url = f"{BASE_URL}/sec_filings/{ticker}?type=10-K&limit=1&apikey={FMP_API_KEY}"
        filings_res = await http_client.get(filings_url)
        filings_data = filings_res.json()

        if not filings_data:
            return {"error": f"No 10-K filing found for {ticker}"}

        filing = filings_data[0]
        filing_url = filing.get("finalLink") or filing.get("link")

        if not filing_url:
            return {"error": f"No filing link found for {ticker}"}

        # Fetch the actual document
        doc_res = await http_client.get(filing_url, follow_redirects=True)
        raw_text = doc_res.text[:15000]  # limit to first 15k chars to stay within token limits

    # Send to Claude for summarization
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a financial analyst. Summarize the following 10-K filing excerpt for {ticker}.

For each key insight, cite the specific section or paragraph it came from.

Structure your response as:
1. Business Overview (cite source)
2. Key Financial Highlights (cite source)
3. Main Risk Factors (cite source)
4. Management Outlook (cite source)

Filing content:
{raw_text}"""
            }
        ]
    )

    return {
        "ticker": ticker,
        "filing_date": filing.get("fillingDate"),
        "filing_url": filing_url,
        "summary": message.content[0].text
    }
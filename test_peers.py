import asyncio
import time
from tools.peers import compare_peers

async def main():
    start = time.time()
    result = await compare_peers("AAPL", ["MSFT", "GOOGL"])
    end = time.time()
    print(f"Time taken: {round(end - start, 2)} seconds")
    print(f"Companies fetched: {len(result['companies'])}")
    for c in result['companies']:
        print(f"  - {c['ticker']}: ${c['revenue']:,} revenue")

asyncio.run(main())

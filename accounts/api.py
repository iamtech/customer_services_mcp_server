import httpx

BALANCE_API_URL = "http://127.0.0.1:8011/getbalance"

async def get_account_balance_api(customer_id: str, account_id: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            BALANCE_API_URL,
            params={"customer_id": customer_id, "account_id": account_id},
            timeout=5.0,
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("balance")
from fastmcp import FastMCP

from accounts.api import get_account_balance_api
from accounts.db import get_customer_accounts

mcp = FastMCP(name="Customer Account MCP Server")

@mcp.resource(uri="customer://{customer_id}/accounts")
def customer_accounts(customer_id: int):
    """
    Returns list of accounts for a customer.
    """
    accounts = get_customer_accounts(customer_id)
    return accounts

@mcp.tool
async def account_balance(customer_id: int, account_id: int):
    """
    Returns account balance from external API.
    """
    balance = await get_account_balance_api(customer_id, account_id)
    return {"balance": balance}

if __name__ == "__main__":
    mcp.run(transport="stdio")
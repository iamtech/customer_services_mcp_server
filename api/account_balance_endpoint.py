from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

fastapi_app = FastAPI(title="Account Balance API")

# Enable CORS
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fastapi_app.get("/getbalance")
async def get_balance(
    customer_id: str = Query(..., description="Customer ID"),
    account_id: str = Query(..., description="Account ID")
):
    """
    Returns account balance for a given customer and account.
    """
    # Simulate fetching balance from a database or external service
    return {"customer_id": customer_id, "account_id": account_id, "balance": 100.0}

if __name__ == "__main__":
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8011, log_level="info")

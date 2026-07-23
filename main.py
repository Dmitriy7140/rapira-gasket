from fastapi import FastAPI
from api.rapira import rapira

app = FastAPI(
    title="Rapira Mirror",
    version="1.0.0",
    description="Used to get Rapira API from a different VPS",
)

@app.get("/open/market/rates")
async def get_market_rates():
    response = rapira.get_usdt_rub()
    return response
from fastapi import FastAPI
from orchestrator import orchestrator

app = FastAPI()

@app.get("/search")
async def search_product(product_name: str):
    top_products = await orchestrator(product_name)
    return top_products

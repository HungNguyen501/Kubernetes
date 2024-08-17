"""API example"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def check_health():
    """Health check API"""
    return {"status": "200 OK"}

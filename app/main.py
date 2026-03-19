from fastapi import FastAPI
from app.orchestrator.orchestrator import Orchestrator

app = FastAPI()
orchestrator = Orchestrator()

@app.post("/alert")
async def alert(data: dict):
    response = await orchestrator.handle_alert(data)
    return response
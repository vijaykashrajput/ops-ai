import asyncio
from .base_agent import BaseAgent

class RAGAgent(BaseAgent):

    async def run(self, data):
        await asyncio.sleep(2)

        return {
            "knowledge": "Similar issue seen before",
            "suggestion": "increase replicas"
        }
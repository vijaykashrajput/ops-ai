from .base_agent import BaseAgent
from app.tools.llm_client import LLMClient
import json
import asyncio


class DebugAgent(BaseAgent):

    async def run(self, data):
        await asyncio.sleep(2)
        llm = LLMClient()

        logs = f"""
        Issue: {data['issue']}
        CPU usage high
        Service slow
        """

        result = llm.analyze_logs(logs)

        try:
            parsed = json.loads(result)
        except:
            parsed = {
                "root_cause": result,
                "severity": "unknown",
                "suggested_fix": "manual check"
            }

        return {
            "analysis": parsed,
            "confidence": 0.9
        }
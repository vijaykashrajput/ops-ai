from .base_agent import BaseAgent

class MonitorAgent(BaseAgent):

    async def run(self, data):
        metric = data.get("metric")
        value = data.get("value")

        if metric == "cpu" and value > 90:
            return {
                "issue": "high_cpu",
                "severity": "high"
            }

        return {
            "issue": "normal",
            "severity": "low"
        }
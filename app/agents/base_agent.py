class BaseAgent:
    async def run(self, data: dict):
        raise NotImplementedError
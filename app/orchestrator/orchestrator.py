import uuid
import asyncio

from app.state.redis_state import RedisStateManager
from app.agents.monitor_agent import MonitorAgent
from app.agents.debug_agent import DebugAgent
from app.agents.fix_agent import FixAgent

class Orchestrator:

    def __init__(self):
        self.state = RedisStateManager()
        self.monitor = MonitorAgent()
        self.debug = DebugAgent()
        self.fix = FixAgent()

    async def handle_alert(self, data):
        workflow_id = str(uuid.uuid4())

        self.state.init(workflow_id, data)

        # Step 1: Monitor (sequential)
        monitor_output = await self.monitor.run(data)
        self.state.update(workflow_id, "monitor", monitor_output)

        # Step 2: Parallel execution (future-ready)
        debug_task = self.debug.run(monitor_output)

        # You can add more agents later
        results = await asyncio.gather(debug_task)

        debug_output = results[0]
        self.state.update(workflow_id, "debug", debug_output)

        # Step 3: Fix (depends on debug)
        fix_output = await self.fix.run(debug_output)
        self.state.update(workflow_id, "fix", fix_output)

        return self.state.get(workflow_id)
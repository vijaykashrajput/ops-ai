import redis
import json

class RedisStateManager:

    def __init__(self):
        self.client = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )

    def init(self, workflow_id, data):
        self.client.setex(
            workflow_id,
            3600,  # 1 hour expiry
            json.dumps({"input": data})
        )

    def update(self, workflow_id, key, value):
        state = self.get(workflow_id)
        state[key] = value
        self.client.set(workflow_id, json.dumps(state))

    def get(self, workflow_id):
        data = self.client.get(workflow_id)
        return json.loads(data) if data else {}
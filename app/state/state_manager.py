class StateManager:
    def __init__(self):
        self.store = {}

    def init(self, workflow_id, data):
        self.store[workflow_id] = {"input": data}

    def update(self, workflow_id, key, value):
        self.store[workflow_id][key] = value

    def get(self, workflow_id):
        return self.store.get(workflow_id, {})
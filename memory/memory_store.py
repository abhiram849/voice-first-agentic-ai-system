class MemoryStore:
    def __init__(self):
        self.history = {}
    
    def update(self, key, value):
        self.history[key] = value

    def get(self, key):
        return self.history.get(key)

    def all(self):
        return self.history

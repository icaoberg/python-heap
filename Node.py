class Node:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def __repr__(self):
        return f"Node({self.value})"

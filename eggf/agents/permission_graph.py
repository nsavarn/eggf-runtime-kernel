class PermissionGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, parent, child, permission):
        if parent not in self.graph:
            self.graph[parent] = []
        self.graph[parent].append((child, permission))

    def get_children(self, node):
        return self.graph.get(node, [])

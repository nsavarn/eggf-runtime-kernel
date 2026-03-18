from eggf.agents.traversal import dfs

class AgentValidator:
    def __init__(self, graph, state_permissions):
        self.graph = graph
        self.state_permissions = state_permissions

    def validate(self, root):
        permissions = dfs(self.graph, root)
        for p in permissions:
            if p not in self.state_permissions:
                return False
        return True

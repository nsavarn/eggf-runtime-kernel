def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    permissions = []

    for child, perm in graph.get_children(node):
        permissions.append(perm)
        if child not in visited:
            permissions.extend(dfs(graph, child, visited))

    return permissions

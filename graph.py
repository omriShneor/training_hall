import typing
from typing import List
from collections import defaultdict, deque

def topological_sort(edges: typing.List[typing.List[int]]) -> typing.List[int]:
    """
    given a list of edges [[v1, v2], [v3,v4], ....] in a directed graph(!)
    find the topological sort of the graph and return that sort. Topological sort in an undirected graph is not well defined.
    """
    adj_list = defaultdict(list)
    indegree = defaultdict(int)

    for child, parent in edges: # i.e in the graph parent -> child
        adj_list[parent].append(child)
        indegree[child]+=1

    queue = deque([v for v in adj_list.keys() if not indegree[v]])
    res = []

    while queue:
        curr = queue.pop()
        for adj_node in adj_list[curr]:
            indegree[adj_node] -= 1
            if not indegree[adj_node]:
                queue.append(adj_node)
        res.append(curr)
    return res

def cycle_detection(edges: typing.List[typing.List[int]]) -> typing.Optional[typing.List[int]]:
    """
    cycle ditection in an undirected graph. This is done by essentially building the adjacency list one edge at a time,
    while running a DFS on the edges and checking if theres a path from u,v other than the current edge we're adding thus
    creating a cycle in the graph.
    """
    def dfs(source, target):
        if source not in seen:
            if source == target:
                return True
            seen.add(source)
            return any(dfs(adj, target) for adj in adj_list[source])

    adj_list = defaultdict(set)
    for u, v in edges:
        seen = set()
        if u in adj_list and v in adj_list and dfs(u, v):
            return u,v

        adj_list[u].add(v)
        adj_list[v].add(u)
    return None

class DSU:
    """
    A DSU data structure can be used to maintain knowledge of the connected components of a graph, and query for them quickly. 
    In particular, we would like to support two operations:
    dsu.find(node x), which outputs a unique id so that two nodes have the same id if and only if they are in the same connected component.
    dsu.union(node x, node y), which draws an edge (x, y) in the graph, connecting the components with id find(x) and find(y) together.
    """
    def __init__(self, n: int) -> None:
        self._parent = [-1] * n

    def find_parent(self, x: int):
        while self._parent[x] >= 0:
                x = self._parent[x]
        return x   

    def union(self, x, y):
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)

        if parent_x == parent_y:
            return False
        elif self._parent[parent_x] < self._parent[parent_y]:
            self._parent[parent_x] += self._parent[parent_y]
            self._parent[parent_y] = parent_x
        else:
            self._parent[parent_y] += self._parent[parent_x]
            self._parent[parent_x] = parent_y
        return True
    
    def cycle_detection(self, edges: typing.List[typing.List[int]]):
        answer = []
        for u, v in edges:
            if not self.union(u,v):
                return [u,v]
        return answer

    def is_tree(self, edges: List[List[int]]):
        for u, v in edges:
            if not self.union(u,v):
                return False
        return False if len([p for p in self._parent if p < 0]) > 1 else True

    



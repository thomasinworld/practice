class Solution:
    # Use Union-Find (Disjoint Set) data structure, which is perfect for detecting cycles in undirected graphs
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize each node as its own parent (1-based indexing)
        n = len(edges)
        parent = list(range(n + 1))
        
        # Find function - finds the root parent of a node with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Union function - unites two components
        def union(x, y):
            parent[find(x)] = find(y)
        
        # Process edges
        for edge in edges:
            x, y = edge
            # If nodes already have the same parent, we found our cycle
            # This must be the redundant edge since we process edges in order
            if find(x) == find(y):
                return edge
            union(x, y)
        
        return [] 

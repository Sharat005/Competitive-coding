class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
    
        if len(edges) != n - 1: return False

        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = {0}
        queue = collections.deque([0])

        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                queue.append(neighbour)

        return len(seen) == n
                
#         graph = {i: [] for i in range(n)}
        
#         # Need to create an adjacencey list
#         for i in range(len(edges)):
#             firstVertice, secondVertice = edges[i]
            
#             graph[secondVertice].append(firstVertice)
#             graph[firstVertice].append(secondVertice)
        
#         queue = deque([0])
#         seen = {0}
        
#         while queue:
#             curr = queue.popleft()
            
#             for i in graph[curr]:
                
                
#                 seen.add(i)
#                 queue.append(i)

            
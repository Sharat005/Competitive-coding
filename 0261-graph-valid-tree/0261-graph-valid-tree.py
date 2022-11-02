class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(n)}
        
        # Need to create an adjacencey list
        for i in range(len(edges)):
            firstVertice, secondVertice = edges[i]
            
            graph[secondVertice].append(firstVertice)
            graph[firstVertice].append(secondVertice)
        
        queue = deque([0])
        parent = {0: -1}
        
        while queue:
            curr = queue.popleft()
            
            for i in graph[curr]:
                if i == parent[curr]:
                    continue
                if i in parent:
                    return False
                
                parent[i] = curr
                queue.append(i)
                
        return len(parent) == n

            
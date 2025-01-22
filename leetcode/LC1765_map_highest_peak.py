class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        mat = [[0 if cell == 1 else None for cell in row] for row in isWater]
        
        from collections import deque
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()
            current_height = mat[i][j]
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if (0 <= ni < m and 0 <= nj < n and mat[ni][nj] is None):
                    mat[ni][nj] = current_height + 1
                    queue.append((ni, nj)) 
        
        return mat

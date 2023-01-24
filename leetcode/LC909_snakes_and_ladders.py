class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells, label = [None] * (n**2 + 1), 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()
        dist = [-1] * (n * n + 1)
        dist[1], q = 0, [(0, 1)]
        while q:
            d, cur = heapq.heappop(q)
            if d != dist[cur]: continue
            for next in range(cur + 1, min(cur + 6, n**2) + 1):
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1 else next)
                if dist[destination] == -1 or dist[cur] + 1 < dist[destination]:
                    dist[destination] = dist[cur] + 1
                    heapq.heappush(q, (dist[destination], destination))
        return dist[n * n]
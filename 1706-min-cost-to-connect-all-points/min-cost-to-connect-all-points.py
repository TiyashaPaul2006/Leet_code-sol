
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        visited = set()
        min_cost = 0

        # (cost, point_index)
        heap = [(0, 0)]

        import heapq

        while len(visited) < n:
            cost, i = heapq.heappop(heap)

            if i in visited:
                continue

            visited.add(i)
            min_cost += cost

            x1, y1 = points[i]

            # Calculate distances to all unvisited points
            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]

                    distance = abs(x1 - x2) + abs(y1 - y2)

                    heapq.heappush(heap, (distance, j))

        return min_cost

        
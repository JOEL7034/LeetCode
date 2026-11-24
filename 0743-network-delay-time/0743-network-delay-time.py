import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # (elapsed_time, current_node)
        min_heap = [(0, k)]
        shortest_time: dict[int, int] = {}

        while min_heap:
            curr_time, node = heapq.heappop(min_heap)

            if node in shortest_time:
                continue

            shortest_time[node] = curr_time

            for neighbor, weight in graph[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(min_heap, (curr_time + weight, neighbor))

        if len(shortest_time) < n:
            return -1

        return max(shortest_time.values())
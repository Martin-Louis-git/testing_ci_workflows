from collections import deque
import heapq

def binary_search(arr, target):

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def graph_bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

def graph_dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            temp = []
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    temp.insert(0, neighbor)
            stack.extend(temp)

    return visited

def shortest_path(graph: dict[int, list[tuple[int, int]]], start:int):
    shortest: dict[int, int] = {}
    minheap = [(0, start)]
    while minheap:
        dist, node = heapq.heappop(minheap)
        if node in shortest:
            continue
        shortest[node] = dist
        for neighbor, weight in graph.get(node, []):
            if neighbor not in shortest:
                heapq.heappush(minheap, (dist + weight, neighbor))
    return shortest

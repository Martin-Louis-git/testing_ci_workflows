from src.functions import binary_search, graph_bfs, graph_dfs, shortest_path

def test_binary_search():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 6) == -1
    assert binary_search(arr, 1) == 0
    assert binary_search([], 5) == -1

def test_graph_bfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    assert graph_bfs(graph, 'A') == {'A', 'B', 'C', 'D', 'E', 'F'}
    assert graph_bfs(graph, 'D') == {'D', 'B', 'A', 'E', 'C', 'F'}

def test_graph_dfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    assert graph_dfs(graph, 'A') == {'A', 'B', 'D', 'E', 'F', 'C'}
    assert graph_dfs(graph, 'D') == {'D', 'B', 'A', 'C', 'F', 'E'}

def test_shortest_path():
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (2, 2), (3, 5)],
        2: [(0, 1), (1, 2), (3, 8)],
        3: [(1, 5), (2, 8)]
    }
    assert shortest_path(graph, 0) == {0: 0, 1: 4, 2: 1, 3: 9}
    assert shortest_path(graph, 1) == {1: 0, 0: 4, 2: 2, 3: 5}
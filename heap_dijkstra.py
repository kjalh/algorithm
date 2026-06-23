import heapq

graph = {
    'A': [('B', 7), ('C', 3), ('D', 10)],
    'B': [('A', 7), ('E', 2), ('F', 6)],
    'C': [('A', 3), ('B', 1), ('D', 2), ('G', 8)],
    'D': [('A', 10), ('C', 2), ('G', 4), ('H', 5)],
    'E': [('B', 2), ('F', 1), ('I', 4)],
    'F': [('B', 6), ('E', 1), ('I', 3), ('J', 7)],
    'G': [('C', 8), ('D', 4), ('H', 2), ('J', 6)],
    'H': [('D', 5), ('G', 2), ('J', 3)],
    'I': [('E', 4), ('F', 3), ('J', 2)],
    'J': [('F', 7), ('G', 6), ('H', 3), ('I', 2)],
}

def dijkstra(graph, start):
    dis = {node: float('inf') for node in graph}
    dis[start] = 0
    q = [(0, start)]
    
    path = {node: None for node in graph}

    while True:
        if len(q) == 0:
            break

        c_dist, c_node = heapq.heappop(q)
        
        if c_dist > dis[c_node]:
            continue

        for near, weight in graph[c_node]:
            new_dis = c_dist + weight
            
            if new_dis < dis[near]:
                dis[near] = new_dis
                path[near] = c_node
                heapq.heappush(q, (new_dis, near))  
                
    return dis, path


start = input("시작점(A-J): ").upper()
result_dis, result_path = dijkstra(graph, start)

for node in result_dis:
    dis = []
    cur = node
    
    while cur is not None:
        dis.append(cur)
        cur = result_path[cur]
    
    real_dis = " -> ".join(dis[::-1])
    
    print(f"정점 {node} 까지의 최단 거리: {result_dis[node]} | 실제 경로: {real_dis}")

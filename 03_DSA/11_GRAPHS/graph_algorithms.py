# Advanced Graph Algorithms (Topological Sort & Dijkstra's Algorithm)
import heapq
from collections import deque, defaultdict

# 1. Topological Sort (Kahn's Algorithm - BFS)
def topological_sort(num_nodes, edges):
    adj = defaultdict(list)
    in_degree = {i: 0 for i in range(num_nodes)}
    
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
        
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    if len(topo_order) == num_nodes:
        return topo_order
    return []  # Cycle exists

# 2. Dijkstra's Shortest Path (Min-Heap)
def dijkstra(num_nodes, edges, start_node):
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    distances = {i: float('inf') for i in range(num_nodes)}
    distances[start_node] = 0
    min_heap = [(0, start_node)]
    
    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)
        
        if curr_dist > distances[node]:
            continue
            
        for neighbor, weight in adj[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
                
    return distances

def main():
    while True:
        print("\n=== Advanced Graph Algorithms Menu ===")
        print("1. Run Topological Sort (Kahn's Algorithm)")
        print("2. Run Dijkstra's Shortest Path Algorithm")
        print("3. Exit")
        
        choice = input("Choose Option (1-3): ").strip()
        
        if choice == "1":
            try:
                n = int(input("Enter number of nodes: "))
                raw = input("Enter directed edges (Format: u-v u-w): ")
                edges = []
                for pair in raw.split():
                    u, v = map(int, pair.split('-'))
                    edges.append((u, v))
                    
                order = topological_sort(n, edges)
                if order:
                    print("🟢 Valid Topological Order: " + " -> ".join(map(str, order)))
                else:
                    print("🔴 Cycle detected! Topological sort is impossible for cyclic graphs.")
            except Exception as e:
                print("Error: Invalid inputs.", e)
                
        elif choice == "2":
            try:
                n = int(input("Enter number of nodes: "))
                raw = input("Enter weighted edges (Format: u-v-weight): ")
                edges = []
                for item in raw.split():
                    u, v, w = map(int, item.split('-'))
                    edges.append((u, v, w))
                    
                start = int(input("Enter starting node: "))
                distances = dijkstra(n, edges, start)
                print(f"\n🟢 Shortest Distances from Node {start}:")
                for node in sorted(distances.keys()):
                    dist_str = distances[node] if distances[node] != float('inf') else "Unreachable"
                    print(f"  Node {node} : Distance = {dist_str}")
            except Exception as e:
                print("Error: Invalid inputs.", e)
                
        elif choice == "3":
            print("done.")
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()

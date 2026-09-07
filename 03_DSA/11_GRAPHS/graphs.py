# Graph Operations (Adjacency List, BFS, DFS)
from collections import deque, defaultdict

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def display(self):
        if not self.adj:
            print("Graph is empty!")
            return
        print("\n--- Adjacency List ---")
        for node in sorted(self.adj.keys()):
            neighbors = ", ".join(map(str, self.adj[node]))
            print(f"  {node} ──> [ {neighbors} ]")

    # BFS Traversal (Queue FIFO)
    def bfs(self, start_node):
        if start_node not in self.adj:
            return []
        
        visited = set([start_node])
        queue = deque([start_node])
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(str(node))
            
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return order

    # DFS Traversal (Recursive)
    def dfs(self, start_node):
        if start_node not in self.adj:
            return []
        
        visited = set()
        order = []
        
        def _dfs_helper(node):
            visited.add(node)
            order.append(str(node))
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    _dfs_helper(neighbor)
                    
        _dfs_helper(start_node)
        return order

def build_sample_graph():
    # Sample Graph:
    #   0 ─── 1 ─── 3
    #   │     │
    #   2 ─── 4
    g = Graph(directed=False)
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4)]
    for u, v in edges:
        g.add_edge(u, v)
    return g

def main():
    g = build_sample_graph()
    
    while True:
        print("\n=== Graph Operations Menu ===")
        print("1. Display Current Graph (Adjacency List)")
        print("2. Run BFS Traversal (Shortest level search)")
        print("3. Run DFS Traversal (Depth search)")
        print("4. Add Custom Edges from Keyboard (e.g. 0-1 1-2 2-3)")
        print("5. Reset Graph (Create new empty graph)")
        print("6. Exit")
        
        choice = input("Choose Option (1-6): ").strip()
        
        if choice == "1":
            g.display()
            
        elif choice == "2":
            try:
                start = int(input("Enter start node for BFS: "))
                order = g.bfs(start)
                if order:
                    print(f"🟢 BFS Traversal from Node {start}: " + " -> ".join(order))
                else:
                    print(f"Node {start} not found in graph!")
            except ValueError:
                print("Error: Please enter a valid node.")
                
        elif choice == "3":
            try:
                start = int(input("Enter start node for DFS: "))
                order = g.dfs(start)
                if order:
                    print(f"🟢 DFS Traversal from Node {start}: " + " -> ".join(order))
                else:
                    print(f"Node {start} not found in graph!")
            except ValueError:
                print("Error: Please enter a valid node.")
                
        elif choice == "4":
            try:
                raw = input("Enter edges separated by spaces (e.g. 0-1 1-2 2-3): ")
                pairs = raw.split()
                for pair in pairs:
                    u, v = map(int, pair.split('-'))
                    g.add_edge(u, v)
                print("Edges added successfully!")
                g.display()
            except Exception:
                print("Error: Format should be like '0-1 1-2 2-3'")
                
        elif choice == "5":
            g = Graph(directed=False)
            print("Graph reset! New empty graph created.")
            
        elif choice == "6":
            print("Keep rockin the 90-Day DSA challenge! Bye.")
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()


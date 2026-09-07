# Graph Operations (Adjacency List, BFS, DFS)
from collections import deque, defaultdict

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if not self.directed:
            if u not in self.adj[v]:
                self.adj[v].append(u)

    def display(self):
        if not self.adj:
            print("Graph is empty! Add edges first.")
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

def main():
    g = Graph(directed=False)
    
    while True:
        print("\n=== Graph Operations Menu ===")
        print("1. Add Edges (Format: u-v u-w)")
        print("2. Display Adjacency List")
        print("3. Run BFS Traversal")
        print("4. Run DFS Traversal")
        print("5. Reset Graph")
        print("6. Exit")
        
        choice = input("Choose Option (1-6): ").strip()
        
        if choice == "1":
            try:
                raw = input("Enter edges: ")
                pairs = raw.split()
                for pair in pairs:
                    u, v = map(int, pair.split('-'))
                    g.add_edge(u, v)
                print("Edges added successfully!")
                g.display()
            except Exception:
                print("Error: Enter valid format like '0-1 1-2'")
                
        elif choice == "2":
            g.display()
            
        elif choice == "3":
            if not g.adj:
                print("Graph is empty! Add edges first.")
            else:
                try:
                    start = int(input("Enter start node: "))
                    order = g.bfs(start)
                    if order:
                        print(f"🟢 BFS Traversal from Node {start}: " + " -> ".join(order))
                    else:
                        print(f"Node {start} not found in graph!")
                except ValueError:
                    print("Error: Please enter a valid number.")
                    
        elif choice == "4":
            if not g.adj:
                print("Graph is empty! Add edges first.")
            else:
                try:
                    start = int(input("Enter start node: "))
                    order = g.dfs(start)
                    if order:
                        print(f"🟢 DFS Traversal from Node {start}: " + " -> ".join(order))
                    else:
                        print(f"Node {start} not found in graph!")
                except ValueError:
                    print("Error: Please enter a valid number.")
                    
        elif choice == "5":
            g = Graph(directed=False)
            print("Graph reset! Graph is now empty.")
            
        elif choice == "6":
            print("done.")
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()

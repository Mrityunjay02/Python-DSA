# Graph Core Problems (Cycle Detection & Number of Islands)
from collections import defaultdict

# 1. Cycle Detection in Undirected Graph (DFS with Parent pointer)
def has_cycle_undirected(adj):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
        
    for node in list(adj.keys()):
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

# 2. Cycle Detection in Directed Graph (DFS with In-Stack tracking)
def has_cycle_directed(adj):
    visited = set()
    in_stack = set()
    
    def dfs(node):
        visited.add(node)
        in_stack.add(node)
        
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in in_stack:
                return True
                
        in_stack.remove(node)
        return False
        
    for node in list(adj.keys()):
        if node not in visited:
            if dfs(node):
                return True
    return False

# 3. Number of Islands (LeetCode 200 - 2D Grid DFS)
def num_islands(grid):
    if not grid or not grid[0]:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    # Create a copy so original grid is preserved
    g = [list(row) for row in grid]
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or g[r][c] == '0':
            return
        g[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    for r in range(rows):
        for c in range(cols):
            if g[r][c] == '1':
                count += 1
                dfs(r, c)
                
    return count

def main():
    while True:
        print("\n=== Graph Core Problems Menu ===")
        print("1. Check Cycle in Undirected Graph")
        print("2. Check Cycle in Directed Graph")
        print("3. Count Number of Islands (2D Grid)")
        print("4. Exit")
        
        choice = input("Choose Option (1-4): ").strip()
        
        if choice == "1":
            try:
                raw = input("Enter undirected edges: ")
                adj = defaultdict(list)
                for pair in raw.split():
                    u, v = map(int, pair.split('-'))
                    adj[u].append(v)
                    adj[v].append(u)
                    
                if has_cycle_undirected(adj):
                    print("🔴 CYCLE DETECTED in Undirected Graph!")
                else:
                    print("🟢 NO CYCLE in Undirected Graph. Graph is a valid tree/forest.")
            except Exception:
                print("Error: Enter valid edge format like '0-1 1-2'")
                
        elif choice == "2":
            try:
                raw = input("Enter directed edges: ")
                adj = defaultdict(list)
                for pair in raw.split():
                    u, v = map(int, pair.split('-'))
                    adj[u].append(v)
                    
                if has_cycle_directed(adj):
                    print("🔴 CYCLE DETECTED in Directed Graph!")
                else:
                    print("🟢 NO CYCLE in Directed Graph. (Valid Directed Acyclic Graph - DAG)")
            except Exception:
                print("Error: Enter valid edge format like '0-1 1-2'")
                
        elif choice == "3":
            try:
                r = int(input("Enter number of rows: "))
                grid = []
                print("Enter grid rows (strings of 1s and 0s, e.g. 11000):")
                for i in range(r):
                    row_str = input(f"  Row {i+1}: ").strip()
                    grid.append(list(row_str))
                    
                islands = num_islands(grid)
                print(f"🟢 Total Number of Islands: {islands}")
            except Exception as e:
                print("Error:", e)
                
        elif choice == "4":
            print("done.")
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()

import networkx as nx 

tree = nx.DiGraph()
tree.add_edge("S","A")
tree.add_edge("S","B")
tree.add_edge("S","D")
tree.add_edge("A","C")
tree.add_edge("C","D")
tree.add_edge("C","G")
tree.add_edge("D","G")
tree.add_edge("B","D")

class Node:
    def __init__(self,name,path):
        self.name = name 
        self.path = path
        
        
def bfs(tree,start,goal):
    visited = []
    node=Node(start,[start])
    queue=[node]
    
    
    while queue:
        node=queue.pop(0)
        
        if node.name in visited:
            continue
        visited.append(node)
        if node.name==goal:
            return node.path
        else:
            for item in tree.neighbors(node.name):
                node_path=node.path + [item]
                neighbors_node=node(item,node_path)
                queue.append(neighbors_node)                      
                
print(bfs(tree,"S","G"))
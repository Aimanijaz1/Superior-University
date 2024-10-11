#!/usr/bin/env python
# coding: utf-8
Task 1: BFS without Queue & without Node
# In[6]:


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []

def BFS(start):
    visited.append(start)  
    print(start)           

    i = 0
    while i < len(visited): 
        curr = visited[i]    
        for neighbour in tree[curr]:  
            if neighbour not in visited: 
                visited.append(neighbour)  
                print(neighbour)            
        i += 1  

print("Breadth First Search:")
BFS('A')  

Task 2: BFS with Queue & Node
# In[2]:


tree = {'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': [], }

visited = []
queue = []
def BFS(visited, tree, node):
    visited.append(node)
    queue.append(node)
    print(node)
    while queue:
        z = queue.pop(0)
        print(z)

        for neighbour in tree[z]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("Breadth first Search results:")
BFS(visited, tree,)
        


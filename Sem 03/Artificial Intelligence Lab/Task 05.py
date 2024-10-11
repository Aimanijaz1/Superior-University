#!/usr/bin/env python
# coding: utf-8

# In[6]:


def DFS(start):
    stack = []
    visited = set()
    stack.append(start)  #Push the starting point onto the stack.
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            process(current)
            stack.extend(neighbour for neighbour in reversed (get_neighbours(current)) if neighbour not in visited)
            
tree = {'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': [], }

# Process a visited point
def process(vertex):
    print(vertex)

# Function to get neighbours
def get_neighbours(vertex):
    return tree[vertex]
DFS('A')


# In[ ]:





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

1) Inorder Traversal: In this traversal, you first visit the left child, then the current node, and finally the right child. The nodes are visited in ascending order in a binary search tree.
2) Preorder Traversal: Here, you visit the current node first, then the left child, and finally the right child.
3) Postorder Traversal: In this traversal, you first visit the left child, then the right child, and finally the current node.

# In[13]:


tree = {
    'A': ['B', 'C'],  
    'B': ['D', 'E'],  
    'C': ['F', 'G'], 
    'D': [],          
    'E': [],          
    'F': [],          
    'G': []           
}

# Inorder Traversal
def inorder(node):
    if node: 
        if tree[node]: 
            inorder(tree[node][0]) 
        print(node) 
        if len(tree[node]) > 1:  
            inorder(tree[node][1])
            print(node)
            

# Preorder Traversal:
def preorder(node):
    if node:  
        print(node) 
        if tree[node]:  
            preorder(tree[node][0]) 
        if len(tree[node]) > 1:  
            preorder(tree[node][1])  

# Postorder Traversal:
def postorder(node):
    if node:  
        if tree[node]:  
            postorder(tree[node][0])  
        if len(tree[node]) > 1:  
            postorder(tree[node][1])  
        print(node)  

print("Inorder Traversal:")
inorder('A') 

print("\n\nPreorder Traversal:")
preorder('A') 

print("\n\nPostorder Traversal:")
postorder('A') 


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Node:
    def __init__(self, pos: tuple, g: float = 0, h: float = 0):
        self.pos = pos 
        self.g = g
        self.h = h
        self.f = self.g + self.h
        self.parent = None  # Previous node

    def __lt__(self, other):
        return self.f < other.f

class A_Star:
    def __init__(self, map_grid):
        self.open = []  
        self.closed = [] 
        self.map_grid = map_grid
        
    def search(self, start, goal):
        self.open.append(start)
        while self.open:
            self.open.sort()
            current = self.open.pop(0)
            self.closed.append(current)

            if current.pos == goal.pos:
                # Reached goal node
                return self.reconstruct_path(current)

            # Check every neighbor
            neighbors = self.get_neighbors(current)

            for neighbor_pos in neighbors:
                neighbor_node = Node(neighbor_pos)

                if neighbor_node in self.closed:
                    continue

                g = current.g + 1  
                h = self.heuristic(neighbor_node, goal)
                f = g + h

                # Check for a cheaper path
                if neighbor_node in self.open:
                    if neighbor_node.f > f:
                        self.update_node(neighbor_node, g, h, current)
                else:
                    self.update_node(neighbor_node, g, h, current)
                    self.open.append(neighbor_node)  
                    
        return None

    def get_neighbors(self, node):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []

        for dir in dirs:
            neighbor_pos = (node.pos[0] + dir[0], node.pos[1] + dir[1])

            # Check if new pos in bounds
            if (0 <= neighbor_pos[0] < len(self.map_grid) and
                0 <= neighbor_pos[1] < len(self.map_grid[0])):

                # Check if traversable
                if self.map_grid[neighbor_pos[0]][neighbor_pos[1]] != 1:
                    neighbors.append(neighbor_pos)

        return neighbors

    def heuristic(self, node, goal):
        d = abs(node.pos[0] - goal.pos[0]) + abs(node.pos[1] - goal.pos[1])
        return d

    def reconstruct_path(self, goal):
        path = [goal.pos]
        current = goal

        while current.parent:
            path.append(current.parent.pos)
            current = current.parent

        return path[::-1]  # Reverse path

    def update_node(self, node, g, h, current):
        node.g = g
        node.h = h
        node.f = g + h
        node.parent = current  # Set the current node as the parent of the neighbor

# Example grid (0 = walkable, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = Node((0, 0))
goal = Node((len(grid)-1, len(grid[0])-1))

astar = A_Star(grid)
path = astar.search(start, goal)

print("Path from start to goal:", path)


# In[ ]:





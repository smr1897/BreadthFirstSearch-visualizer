from collections import deque

graph = {
    'A' : ['B','E'],
    'B' : ['A','C'],
    'C' : ['B','D'],
    'D' : ['C','E'],
    'E' : ['A','D']
}

def bfs(start,goal,graph):
    queue = deque([start])
    visited = {start:None}

    while queue:
        current_node = queue.popleft()
        if current_node == goal:
            break

        next_nodes = graph[current_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = current_node

    return visited

start = 'A'
goal = 'D'
visited = bfs(start,goal,graph)

current_node = goal
print(f'\npath form {goal} to {start}: \n {goal}' , end='')
while current_node != start:
    current_node = visited[current_node]
    print(f'---> {current_node}', end='')
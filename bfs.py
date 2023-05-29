graph = {
    '5' : ['2','3'],
    '4' : ['1','2'],
    '2' : [],
    '3' : ['5','6'],
    '1' : [],
    '7' : ['1']
    
}

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)

    while queue:  # Creating a loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search:")
bfs(visited, graph, '5')  # function calling

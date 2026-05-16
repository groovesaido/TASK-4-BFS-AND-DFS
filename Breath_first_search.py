#CIT-223-054/2024
#STEPHEN MUIGA KIRAGU
from collections import deque
def bfs(graph,start):
    #storing path taken
    queue=deque([start]) #queue for bfs
    visited=set() #track visited nodes
    visited.add(start)
    while queue:
        node=queue.popleft()
        print(node,end='')
        #visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

#graph
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
bfs(graph,'A')
#CIT-223-054/2024
#STEPHEN MUIGA KIRAGU
def dfs(graph,node,visited=None):
    #storing path taken
    if visited is None:
        visited=set()
    visited.add(node)
    print(node,end='')
    
    #visit all neighbors recursively
    for neighbor in graph[node]:
         if neighbor not in visited:
            dfs(graph,neighbor,visited)

#graph
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
dfs(graph,'A')
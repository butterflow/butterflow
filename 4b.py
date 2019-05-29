def bfs(graph,start,path=[]):
	q=[start]
	while q:
		v=q.pop(0)
		if v not in path:
			path=path+[v]
			q=q+graph[v]
	return path
graph={}
size=int(input("enter noof vertices"))
for i in range(size):
	node=input("enter a node")
	adj=[]
	ad=input("enter adj vertex(enetr -1 to quit)")
	while (ad!='-1'):
		adj.append(ad)
		ad=input("enter adj vertex(enetr -1 to quit)")
	graph[node]=adj
print(graph)
visited=[]
for i in graph:
	visited.append(False)
print(visited)
path=[]
start=input("enter source")
x=bfs(graph,start,path)
print(x)

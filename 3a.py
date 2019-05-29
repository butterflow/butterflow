def dfs(graph,src,visited):
	print(src,"-->",end="")
	visited.append(src)
	for i in graph[src]:
		if i not in visited:
			dfs(graph,i,visited)
graph={}
n=int(input("moof edges"))
for i in range(0,n):
	start=input("enter start vertes")
	end=input("enter end vertex")
	try:
		graph[start].append(end)
	except KeyError:
		graph[start]=[end]
	try:
		graph[end].append(start)
	except KeyError:
		graph[end]=[start]
src=input("enetr source vertex")
dfs(graph,src,visited=[])
orint("\b\b\b  ")
	

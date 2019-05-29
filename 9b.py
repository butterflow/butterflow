def prims():
	global n,graph
	visited=[0 for i in range(n)]
	ne=1 ; visited[0]=1
	mincost=0
	while ne < n:
		minn=999
		for i in range(n):
			for j in range(n):
				if graph[i][j]<minn and visited[i]!=0:
					minn=graph[i][j]
					u=i ; v=j
		if visited[v]==0:
			print(u,"--->",v,":",minn)
			visited[v]=1
			ne+=1
			mincost+=minn
		graph[u][v]=999

	print("Minimum Cost=",mincost)

n=int(input("Enter number of nodes:"))
graph=[[]for i in range(n)]
for i in range(n):
	for j in range(n):
		print("Enter cost b/w nodes",i+1,"and",j+1)
		val=int(input())
		graph[i].append(val)
print("GRAPH:",graph)
print("---MINIMUM SPANNING TREE---")
print("EDGE     : COST")
prims()

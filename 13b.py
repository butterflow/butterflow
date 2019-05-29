def bf(s):
	global graph,n
	d=[999 for i in range(n+1)]
	d[s]=0
	for i in range(n-1):
		for pair in graph:
			d[pair[1]]=min(d[pair[1]],d[pair[0]]+pair[2])
	del d[0]
	return d

graph=[]
n=int(input("Enter number of nodes:"))
e=int(input("Enter number of edges:"))
for i in range(e):
	u=int(input("Enter node u:"))
	v=int(input("Enter node v:"))
	c=int(input("Enter cost:"))
	graph.append((u,v,c))
print("Graph:",graph)
source=int(input("Enter source node:"))
d=bf(source)
print("---Single Source Shortest Path Tree---")
print("EDGE     : COST")
for i in range(n):
	print(source,"--->",i+1,":",d[i])

def kruskals():
    global n, graph
    parent = [0 for i in range(n + 1)]
    ne = 0;
    mincost = 0
    while ne != n - 1:
        minn = 999
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # print(i,j)
                if graph[i][j] < minn:
                    minn = graph[i][j]
                    u = i;
                    v = j
                    a = i;
                    b = j
        while parent[u] != 0:
            u = parent[u]
        while parent[v] != 0:
            v = parent[v]
        if u != v:
            print(a, "--->", b, ":", minn)
            mincost += minn
            ne += 1
            parent[v] = u
        graph[a][b] = graph[b][a] = 999
    print("Minimum Cost=", mincost)


n = int(input("Enter number of nodes:"))
graph = [[0] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("Enter cost b/w nodes", i, "and", j)
        val = int(input())
        graph[i].append(val)
print("GRAPH:", graph)
print("---MINIMUM SPANNING TREE---")
print("EDGE     : COST")
kruskals()

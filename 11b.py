n=int(input("Enter number of items:"))
items=list(range(0,n+1))
weights=[0]
values=[0]
for i in range(1,n+1):
	print("Enter weight of item",i)
	w=int(input())
	print("Enter value of item",i)
	v=int(input())
	weights.append(w)
	values.append(v)
W=int(input("Enter Knapsack capacity:"))


M=[[0 for j in range(W+1)]for i in range(n+1)]
for i in range(1,n+1):
	for w in range(1,W+1):
		if weights[i]>w:
			M[i][w]=M[i-1][w]
		else:
			M[i][w]=max(M[i-1][w],values[i]+M[i-1][w-weights[i]])

Knapsack=[]
i=n ; k=W
while i>0 and k>0:
	if M[i][k]!=M[i-1][k]:
		Knapsack.append(i)
		k-=weights[i]
		i-=1
	else:
		i-=1
print("---Items in Knapsack---")
print("ITEM : WEIGHT : VALUE")
for i in range(len(Knapsack)):
	print(Knapsack[i],"   :",weights[Knapsack[i]],"     :",values[Knapsack[i]])
print("Maximum Value achieved:",M[n][W])

c=0
def mergesort(list):
	if len(list)<2:
		return list
	mid=len(list)//2
	l=list[:mid]
	r=list[mid:]
	return merge(mergesort(l),mergesort(r))
def merge(l,r):
	i=0
	j=0
	list=[]
	global c
	while i<len(l) and j<len(r):
		if l[i]<r[j]:
			list.append(l[i])
			i=i+1
		else:
			list.append(r[j])
			j=j+1
			c=c+(len(l)-i)
			print("inv",c)
	list.extend(l[i:])
	list.extend(r[j:])
	return list
p=[1,4,3,2,6,5]
print(p)
x=mergesort(p)
print(x)
print("noof inv",c)

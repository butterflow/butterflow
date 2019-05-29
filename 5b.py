def mergesort(list):
	if len(list)>1:
		mid=len(list)//2
		l=list[:mid]
		r=list[mid:]
		mergesort(l)
		mergesort(r)
		i=0
		j=0
		k=0
		while i<len(l) and j<len(r):
			if l[i]<r[j]:
				list[k]=l[i]
				i=i+1
				k=k+1
			else:
				list[k]=r[j]
				j=j+1
				k=k+1
		while i<len(l):
			list[k]=l[i]
			i=i+1
			k=k+1
		while j<len(r):
			list[k]=r[j]
			j=j+1
			k=k+1
	return list
p=[1,4,3,2,6,5]
print(p)
mergesort(p)
print(p)

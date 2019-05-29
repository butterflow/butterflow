import time,random
def bsort(l):
	for i in range(len(l)):
		for j in  range(0,(len(l)-i-1)):
			if l[j]>l[j+1]:
				l[j],l[j+1]=l[j+1],l[j]
	return l
x=[random.randint(1,10) for i in range(10)]
print(x)
start=time.time()
f=bsort(x)
end=time.time()
print("sorted array is:")
print(f)
print("time is:",(end-start))

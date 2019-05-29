import time,random
def ssort(l):
	for i in range(len(l)-1):
		min=i
		for j in range(i+1,len(l)):
			if l[j]<l[min]:
				min=j
		l[i],l[min]=l[min],l[i]
	return l
x=[random.randint(1,10) for i in range(10)]
print(x)
start=time.time()
f=ssort(x)
end=time.time()
print("sorted array is:")
print(f)
print("time is:",(end-start))

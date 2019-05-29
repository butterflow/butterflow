import time
import random
def isort(arr):
	for i in range(1,len(arr)):
		key=arr[i]
		j=i-1
		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key
	return arr
f=[random.randint(1,10)for i in range(10)]
print(f)
start=time.time()
isort(f)
end=time.time()
print("sorted array:")
print(f)
print("time taken is:",(end-start))


import time
def binary(arr,l,h,k):
	if(l<=h):
		mid=(l+h)//2
		if(arr[mid]==k):
			return mid
		elif(arr[mid]>k):
			return binary(arr,l,mid-1,k)
		else:
			return binary(arr,mid+1,h,k)
	return -1
n=10
l=[]
for i in (range(n)):
	l.append(i)
x=int(input("enter key to be searched"))
start=time.time()
f=binary(l,0,n-1,x)
end=time.time()
if(f==-1):
	print("key not found")
else:
	print("the key is found at %d location",f)
	print("time taken is %d",(end-start))


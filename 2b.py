import time
freemen=[]
menpref={}
womenpref={}
num=int(input("enter noof men and women"))
for m in range(num):
	key=input("enter key")
	freemen.append(key)
	for n in range(num):
		val=input("enter value")
		menpref.setdefault(key,[])
		menpref[key].append(val)
print(menpref)
for m in range(num):
	key=input("enter key")
	for n in range(num):
		val=input("enter value")
		womenpref.setdefault(key,[])
		womenpref[key].append(val)
print(womenpref)
takenwomen=[]
final={}
start=time.time()
while freemen!=[]:
	for i in freemen:
		listofw=menpref.get(i)
		for j in listofw:
			if j not in takenwomen:
				final[j]=i
				freemen.remove(i)
				takenwomen.append(j)
				break
			else:
				listofm=womenpref.get(j)
				r=final.get(j)
				p=listofm.index(i)
				q=listofm.index(r)
				if p<q:
					final[j]=i
					freemen.remove(i)
					freemen.append(r)
					takenwomen.append(j)
					break
print(final)
end=time.time()
print("time is:",(end-start))



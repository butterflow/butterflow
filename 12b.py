def predecessor():
	global jobs,n
	cur=n
	chosen=cur-1
	while cur>1:
		if chosen<=0:
			p[cur]=0
			cur-=1
			chosen=cur-1
		else:
			if jobs[cur][0]>=jobs[chosen][1]:
				p[cur]=chosen
				cur-=1
				chosen=cur-1
			else:
				chosen-=1

def find_sol(j):
	global Schedule
	if j>0:
		if jobs[j][2]+M[p[j]]>M[j-1]:
			Schedule.append(j)
			find_sol(p[j])
		else:
			find_sol(j-1)

n=int(input("Enter number of intervals:"))
jobs=[0]
for i in range(1,n+1):
	print("Enter start and finish time of job",i)
	s=int(input())
	f=int(input())
	print("Enter value of job",i)
	v=int(input())
	jobs.append((s,f,v))

p=[0 for i in range(n+1)]
predecessor()

M=[0 for i in range(n+1)]
for i in range(1,n+1):
	M[i]=max(jobs[i][2]+M[p[i]],M[i-1])

Schedule=[]
find_sol(n)

Schedule.sort()
print("---SCHEDULE---")
print("NO. : START : FINISH : VALUE")
for i in range(len(Schedule)):
	print(Schedule[i],"  :",jobs[Schedule[i]][0],"    :",jobs[Schedule[i]][1],"     :",jobs[Schedule[i]][2])
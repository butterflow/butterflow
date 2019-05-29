n0=0
c=7
print("Value of c=",c)
print("n | f(n) | c*g(n)")
for n in range(10,31):
	fn=6*n*n+2*n+2
	gn=c*n*n
	if fn<=gn and n0==0:
		n0=n
	print(n," ",fn,"   ",gn)
print("n0=",n0)

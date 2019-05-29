n0=0
c1=7
c2=5
print("Value of c1=",c1)
print("Value of c2=",c2)
print("n | f(n) | c1*g(n) | c2*g(n)")
for n in range(10,31):
	fn=5*n*n+6*n+3
	gn1=c1*n*n
	gn2=c2*n*n
	if fn>=gn2 and fn<=gn1 and n0==0:
		n0=n
	print(n," ",fn,"   ",gn1,"   ",gn2)
print("n0=",n0)

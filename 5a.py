print	("The	function	is	7n^2	+	7n	+	5")
print	("G(n)	=	n^2	")
print	("Assuming	c1	as	6	and	c2	as	8")
for	i	in	range	(30):
			a1	=	7*(i**2)+7*i+5
			a2	=	6*(i**2)
			a3	=	8*(i**2)
			if	a1>=a2	and	a3>=a1:
							n0	=	i
							break
print	("The	value	of	n0:	",	n0)
print	("n	\t\t	F(n)	\t\t	c1*G(n)	\t\t	c2*G(n)")
for	i	in	range	(10,31):
			a1	=	7*(i**2)+7*i+5
			a2	=	6*(i**2)
			a3	=	8*(i**2)
			print	(i,"\t\t",a1,"\t\t",a2,	"\t\t",	a3)
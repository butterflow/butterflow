print	("The	function	is	3n^2	+	4n	+	3")
print	("G(n)	=	n	")
print	("Assuming	c	as	10")
for	i	in	range	(30):
			a1	=	3*(i**2)+4*i+3
			a2	=	10*i
			if	(a1>=a2):
							n0	=	i
							break
print	("The	value	of	n0:	",	n0)
print	("n	\t\t	F(n)	\t\t	c*G(n)")
for	i	in	range	(10,31):
			a1	=	3*(i**2)+4*i+3
			a2	=	10*i
			print	(i,"\t\t",a1,"\t\t",a2)
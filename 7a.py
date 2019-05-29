print	("The	function	is	2n^2	+	3n	+	5")
print	("G(n)	=	n	")
print ("Assuming	c	as	9")
for	i	in	range	(30):
			a1	=	2*(i**2)+3*i+5
			a2	=	19*i
			if	(a1>=a2):
							n0	=	i
							break
print	("The	value	of	n0:	",	n0)
print	("n	\t\t	F(n)	\t\t	c*G(n)")
for	i	in	range	(10,31):
			a1	=	2*(i**2)+3*i+5
			a2	=	9*i
			print	(i,"\t\t",a1,"\t\t",a2)
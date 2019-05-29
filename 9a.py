print("Your function is 8n^2+3n+3")
print ("g(n) = n^2 ")
print("Assuming c as 7")
for i in range (30):
 a1 = 8*(i**2)+3*i+3
 a2 = 7*(i**2)
 if (a1>=a2):
 n0 = i
 break
print("Value of n0: ", n0)
print ("Value\t\tF(n)\t\tc*G(n)")
for i in range (10,31):
 print (i,"\t\t",8*(i**2)+3*i+3,"\t\t",7*(i**2))
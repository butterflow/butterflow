print("Your function is 8n^2+3n+3")
print ("g(n) = n^2 ")
print("Assuming c as 9")
n=0
for i in range (30):
    a1 = 8*(i**2)+3*i+3
    a2 = 10*(i**2)
    if (a2>=a1):
        n=i
    break
print("Value of n0: ",n)
print ("Value\t\tF(n)\t\tc*G(n)")
for i in range (10,31):
    print (i,"\t\t",8*(i**2)+3*i+3,"\t\t",9*(i**2))
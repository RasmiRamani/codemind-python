n=int(input())
s=0
a=n**2
num=a%10
num2=a%100
num3=a%1000
if n==num or n==num2 or n==num3:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
     

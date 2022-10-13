n=int(input())
s=0
a=n**2
q=a%10
w=a%100
r=a%1000
if n==q or n==w or n==r:
   print('Automorphic Number')
else:
    print('Not an Automorphic Number')
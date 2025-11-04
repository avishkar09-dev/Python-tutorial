#Basic while loop code
'''i=1
while(i<=5):
    print(i)
    i=i+1'''

#Factorial Code
'''num=int(input("Enter the number:"))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i=i+1   
print(fact)'''

#To find number of digit user enter
'''n=int(input("Enter the number:"))
c=0
while(n!=0):
    n=n//10
    c=c+1
print(c)'''

'''n=int(input("Enter any number:"))
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
print(l)'''

#Perfect Numbers
'''n=int(input("Enter any number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
print(sum)
if sum==n: 
    print("Perfect number")
else:
     print("Not perfect number")'''

#To print sum of digits in a positive number n>0
'''n=int(input("Enter any number"))
a=n
sum=0
while(n!=0):
    last=n%10
    sum=sum+last
    n=n//10
print("The sum of digits in",a,"is",sum)'''

#To find strong number code
'''n=int(input("Enter number :"))
a=n
sum=0
while(n!=0):
    last=n%10
    fact=1
    for i in range(1,last+1):
        fact=fact*i
        sum=sum+fact
        n=n//10
if sum==a:
    print("Strong number")
else:
    print("Not strong number")'''









        





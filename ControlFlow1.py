'''num=int(input("Enter a number:"))
if(num%2==0):
    print("Number is even")
else:
    print("number is odd")'''

#For loop:
'''for x in "pankaj":
    print(x)'''

'''i=0
for x in "Panlaj":
    print("the element at index",i,"is ",x) 
    i=i+1'''

'''for i in range(5):
    print("Pankaj")'''

'''n=1
for i in range(1,6):
    n=n*i
    print(n)'''

'''num=int(input("Enter your number:"))
fact=1
for num in range(1,num+1):
    fact=fact*num
print(fact)'''

# Code to find Prime numbers:
'''num=int(input("Enter your numbers:"))
if(num<=1):
        print("Not prime")
else:
     for i in range(2,int(num**0.5)+1):
        if(num%i==0):
             print("Not prime")
             break
     else:
          print("Prime")'''

'''a=int(input("Enter starting point:"))
b=int(input("Enter End point:"))
for i in range(a,b):
    if i > 1:
         for j in range(2,i):
              if(i%j==0):
                    break    
         else:
            print(i,end=" ")'''

#to find factors of any number
n=int(input("Enter any number:"))
for i in range(1,n+1):
    if(n%i==0):
        print(i)

        
             
         
   
         
   
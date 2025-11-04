'''for i in range(1,4):
    for j in range(1,5):
        print(i,j)'''

'''for i in range(1,4):
    for j in range(1,5):
        print(i,j,sep="",end=" ")
    print()'''

'''for row in range(1,6):
    for col in range(1,row+1):
        print(col,sep='',end='')
    print()   '''

'''n=int(input("Enter your number:"))
for row in range(1,n+1):
    print(' '*(n-row),end='')
    print('*'*(2*row-1))
for row in range(n-1,0,-1):
    print(' '*(n-row),end='')
    print('*'*(2*row-1))'''

#Fibonacci sequence
'''n=int(input("Enter any number:"))
a,b=0,1
print(a,b , end=' ')
for i in range(n - 2):
    c=a+b
    print(c ,end=' ')
    a,b=b,c'''

'''n=int(input("Enter number:"))
a,b=0,1
for i in range(n):
    print(a ,end=" ")
    a,b=b,a+b'''


'''n=6
start=1
for row in range(1,n+1):
    print(' '*(n-row),end="")
    
    val=start
    for col in range(row):
        print(f"{val}",end="")
        val+=2
        
    start += row*2
    print()'''

'''n=int(input("Enter number:"))
for row in range(1,n+1):
    print(" "*(n-row),end="")
    for col in range(1,row+1):
        print(col,sep="",end="")
    print()'''


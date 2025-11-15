# Aliasing ==> use = operator to make 2 list equal but it makes id also same

'''x=[1,2,3,4]
y=x
print(y)
print(id(x))
print(id(y))

# so id and value will be same for both x and y and if we make any changes in x then changes will happen in y also.
# so t avoid these changes we can use copy or slicing method  ==> cloning

a=[10,20,30,40]
b=a[:]
print(b)

# OR

c=a.copy()
print(c)
print(id(a))
print(id(b))
print(id(c))


# relational oprator
l1=[1,2,3]
l2=[1,2,4]
print(l1<l2) # 1,1  2,2  3<4 ==>True

# clear ==> remove all the elements from the list

l=[1,2,3,4]
l.clear()
print(l) # print empty list

# A list can be a member of another list

l=[[1,2,3],[4,5,6],["Pankaj",7,8]]
print(l[0]) # [1,2,3]
print(l[0][1]) # 2'''

# matrix
dimensions=input().split()
m=int(dimensions[0])# rows
n=int(dimensions[1])# columns
l=[]# 2d list
for i in range(m):# need not to worry about n
    new_row=[int(i) for i in input().split()]
    l.append(new_row)
print(l)













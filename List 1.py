# List is mutable, duplicate allowed, slicing possible, indexing possible, dynamic in nature, group of heterogeneous 
'''
l=list(range(1,6))
print(l)

l=[]
s=input().split()
for element in s:
    l.append(int(element))
print(l)

l=[]
n=int(input())
for i in range(n):
    inp=int(input())
    l.append(inp)
print(l)

l=[]
for i in range(5):
    l.append(0)
print(l)

# OR

l=[ 0 for i in range(5)]
print(l)

l=[i for i in range(5)]
print(l)

l=[2*i for i in range(5)]
print(l)

# Adding elements ==> append, insert, extend
# append & insert ==> add 1 element
# extend ==> we can add element of one list at the end of other list

l=[]
l.insert(0,100)
print(l)

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a) # Output ==> [1,2,3,4,5,6]
print(b) # Output ==> [4,5,6] 

# delete ==> remove ==> it removes 1st occurence of element & pop ==> it removes and returns the last element from the list

l=[1,2,3,4,1,6,4,4]
l.remove(4)
print(l)

a=[1,2,3,4]
print("Original list is",a)
l=a.pop()
print("Element removed is",l)
print("New list is",a)

# del is use to delete variable

# len(), index(), count()

l=[1,2,3,4,"Neeraj"]
print(len(l))

if "Neeraj" in l:
    i=l.index("Neeraj")
    print(i)
else:
    print("Element is not present")

# reverse(), sort()

l=[1,2,3,4]
l.reverse()
print(l)

l=[10,0,50,-90]
l.sort()
print(l)

l=['shyam','ram',] # Alphabetical order 
l.sort()
print(l)

a=[1,2,3,-3,0,-900]
a.sort(reverse=True)
print(a)'''




















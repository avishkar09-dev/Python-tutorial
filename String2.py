'''# Split ==> Divides a string into two parts based on a specified separator.
s= "Hello welcome to the world of Python programming."
l=s.split()
print(l)  # Output: ['Hello', 'welcome', 'to', 'the', 'world', 'of', 'Python', 'programming.']
 # default separator is space

a = "09/10/2023"
b=a.split("/")
print(b)  # Output: ['09', '10', '2023']

# Join ==> Combines a list of strings into a single string, with a specified separator between each element.
l=["Hello", "welcome", "to", "the", "world", "of", "Python", "programming."]
j=" ".join(l)
print(j)  # Output: "Hello welcome to the world of Python programming."

S= "Hello welcome to the world of Python programming."
for word in s.split():
    if (len(word)%2==0):
        print(word)

s=input()
a=s.split()
updated=[]
for word in a[:len(a)-1]:
    updated.append(word[0])
updated.append(a[len(a)-1])
updated=' '.join(updated)
print(updated) 

# find() ==> it returns index first occurence of substring, if it is not present returns -1
s="pankaj sir is pankaj sir"
print(s.find("pankaj"))

# Another version of find(substring,start index,end index) we can tell from where to start
print(s.find("pankaj",10,30))

# index() ==> but if the substring is not available ==> value error(error)

# rfind ==> returns index of last occuerncce 

# finding/counting substring==> count()
s="pankaj sir is pankaj sir"
print(s.count("pankaj")) # total number of occurences in s
print(s.count("pankaj",1,len(s)))

# type 1
s=input()
a=s.split()
updated=[]
for word in a[::-1]:
    updated.append(word)
updated=' '.join(updated)
print(updated)

# type 2
t=input().split()
x=' '.join(t[::-1])
print(x)

t=input().split()
l=[]
for word in t:
    l.append(word[::-1])
x=' '.join(l)
print(x)'''

# startwith() ==> Checks if string starts with substring
# endswith() ==> Checks if string ends with substring
# upper() ==> converts to uppercase
# lower() ==> converts to lowercase
# swapcase() ==> swaps case of all characters
# isalnum() ==> returns true if string is alphanumeric a-z, A-Z, 0-9
# isalpha() ==> returns true if all are alphabets
# isdigit() ==> returns true if all are digits
# isspace() ==> returns true if all are whitespace characters

# format() ==> formats specified values in a string
name = "Pankaj"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {1} and I am {0} years old.".format(age, name))
print("My name is {n} and I am {a} years old.".format(n=name, a=age))

# f-strings ==> formatted string literals
print(f"My name is {name} and I am {age} years old.")


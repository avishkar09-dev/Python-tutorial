''' Use triple quotes to print multilines  

a='This is \'single quote and we are printing it'
print(a) 

s='pankaj'
for i in range(len(s)):
    print(i,s[i])
    print(i-len(s),s[i-len(s)]) 

# Slicing s[start:end:step]
s='pankaj'
print(s[:])
print(s[4:2:-1]) # 4 to 2+1 when it is reverse 

# If it is positive ==> it should be in forward direction
# If it is negative ==> it should be in reverse direction 
# backward direction always add +1

print(s[1:4:-1]) # Empty string
print(s[-2:-5:-1])
print(s[::-1]) # Reverse string 
  
# Multiply operator in case of string use for repetition os string

#Use of membership operator ==> in
s=input("Enter the string:")
t=input("Enter the substring you want to find:")
if t in s:
    print("YES")
else:
    print("NO")

# palindrome for one word
s=input("Enter the string:")
if s[::-1]==s:
    print("palindrome")
else:
    print("not palindrome")'''

# comparison and capital letters are different from small letters
# print("Ramesh">"ramu")

# Removing spaces in string
# strip ==> remove spaces from beg as wll as end & rstrip ==> remove spaces from end and lstrip ==> remove spaces from beg

s= "   pankaj   "
updated=s.strip() # Only for string
print(len(s))
print(updated)
print(len(updated))




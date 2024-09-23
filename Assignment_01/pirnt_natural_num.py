# x=int(input("Enter a number "))

# for i in range(1,x):
#     print(i,end=' ')



# Python For Loop with String
# s =" welcome to first program"
# for i in s:
#     print(i,end='')

# Python for loop with Range
# for i in range(0,10,2):
#     print(i,end=' ')

# Python for loop Enumerate
# i1=["Eat","Read","sleep","Repeat"]
# for count,el in enumerate(i1):
#     print(count,el)

# Nested For Loops in Python
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

# n=int(input("Enter a number you want to print a table "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# Python For Loop Over List
# l=["welcome","to","my","program"]
# for i in l:
#     print(i)

# Python for loop in One Line
# num =[ x for x in range(11)]
# print(num)

# Python For Loop with Tuple
# t=((1,2),(2,3),(3,4))
# for a,b in t:
#     print(a,b)

# fruit=["Apple","Banana","cheryy"]
# clour=["Red","yellow","green"]
# for fruit,clour in zip(fruit,clour):
    # print(fruit,"is",clour)

# Continue in Python For Loop
for letter in 'geeksforgeeks':
    if letter =='e' or letter =='s':
        continue
    print('curren letter ',letter)
        

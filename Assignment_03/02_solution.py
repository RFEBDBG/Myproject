age=int(input("Enter your age :"))
day=input("Enter Day :")
if age>=18 and day!='wednesday':
    price =12
elif age>=18 and day=='wednesday':
    price=10
elif age<18 and day=='wednesday':
    price =6
else:
    price=8
print(price)




Score=int(input("Enter a Score :"))
if Score>100:
    print("please check your score:")
    exit()
if Score>=90 and Score<=100:
    print("Grade--> A")
elif Score>=80 and Score<=89:
    print("Grade--> B")
elif Score>=70 and Score<=79:
    print("Grade--> C")
elif Score>=60 and Score>=69:
    print("Grade--> D")
else:
    print("Grade--> F")
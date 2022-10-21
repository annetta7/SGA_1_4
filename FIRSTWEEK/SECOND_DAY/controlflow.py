#if statement practice
grade = 69
if grade > 60:
    print("B")
else:
    print("failed")



print("I'll execute either way")

grade = 50
if grade > 60:
    print("B")
else:
    print("failed")


print("I'll execute either way")


grade = 50
if grade > 60:
    print("B")
elif grade >= 50 and grade <= 59:
    print("C")
else:
    print("failed")


grade = 39
if grade >= 70:
    print("A")
elif grade >= 60 and grade <= 69:
    print("B")
elif grade >= 50 and grade <=59:
    print("C")
elif grade >= 40 and grade <=49:
    print("D")
else:
    print("failed")



    

x = int(input("Please input your grade:"))
if type(x) == int:
    
    if x >= 70:
        print("A")
    elif x >= 60 and x <= 69:
        print("B")
    elif x >= 50 and x <= 59:
        print("C")
    elif x >= 40 and x <= 49:
        print("D")
    else:
        print("failed")

else:
    print("Our program only accepts integer values")

print("I will execute either way")




x = input("Please input your grade")
if type(x) == int:
    
    if x >= 70:
        print("A")
    elif x >= 60 and x <= 69:
        print("B")
    elif x >= 50 and x <= 59:
        print("C")
    elif x >= 40 and x <= 49:
        print("D")
    else:
        print("failed")

else:
    print("Our program only accepts integer values")

print("I will execute either way")
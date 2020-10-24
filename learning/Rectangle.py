n=str(input("Enter your name:"))
p=str(input("Enter Password:"))
if (p=="Avengers"):
    print("1.Area of Rectangle")
    print("2.Perimeter of Rectangle")
    ch=int(input("Choose one option:"))

    if ch==1:
        answer=0
        l=int(input("Enter length of Rectangle:"))
        b=int(input("Enter breadth of Rectangle:"))
        answer=l*b
        print("The Area of the Rectangle is",answer)

    elif ch==2:
        answer=0
        l=int(input("Enter length of Rectangle:"))
        b=int(input("Enter breadth of Rectangle:"))
        answer=(l*2)+(b*2)
        print("The Area of the Rectangle is",answer)
else:
    print("Wrong Password",n)
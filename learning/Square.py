n=str(input("Enter your name:"))
p=str(input("Enter Password:"))
if (p=="Avengers"):
    print("1.Area of Square")
    print("2.Perimeter of Square")
    ch=int(input("Choose one option:"))

    if ch==1:
        answer=0
        a=int(input("Enter side of the square:"))
        answer=a*a
        print("Area of the square:",answer)

    elif ch==2:
        answer=0
        a=int(input("Enter side of the square:"))
        answer=a*4
        print("Perimeter of the square:",answer)
else:
    print("Wrong Password",n)
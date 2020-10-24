n=str(input("Enter your name:"))
p=str(input("Enter Password:"))
if (p=="Avengers"):
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    ch=int(input("Choose one option:"))
    if ch==1:
        sum=0
        count=int(input("How many numbers do you want?:"))
        for i in range(count):
            x=float(input("Enter number:"))
            sum=sum+x
        print("The sum is", sum)

    elif ch==2:
        difference=0
        count=int(input("How many numbers do you want?:"))
        for i in range(count):
            x=float(input("Enter number:"))
            difference=difference-x
        print("The difference is", difference) 

    elif ch==3:
        product=0
        count=int(input("How many numbers do you want?:"))
        for i in range(count):
            x=float(input("Enter number:"))
            product=product*x
        print("The product is", product)

    elif ch==4:
        quotient=0
        count=int(input("How many numbers do you want?:"))
        for i in range(count):
            x=float(input("Enter number:"))
            quotient=quotient/x
        print("The quotient is", quotient)
else:
    print("Wrong Password", n)
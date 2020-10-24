n=str(input("Enter your name:"))
p=str(input("Enter Password:"))
if (p=="Avengers"):
    num=int(input("Enter a number:"))
    print("Factors of the given number {0} are".format(num))
    for value in range (1,num+1):
        if (num%value == 0):
            print("{0}" .format(value))
else:
    print("Wrong Password",n)
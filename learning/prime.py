a=int(input("Enter a number:"))
isprime=True
if a>1:
    for i in range(2,a):
        if (a%i)==0:
            isprime=False
            break
        if isprime==True:
            print(a,"is a prime number")
        else:
            print(a,"is not a prime number")
else:
    print(a,"is not a prime number")
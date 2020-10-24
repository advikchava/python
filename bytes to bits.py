n=str(input("Enter your name:"))
p=str(input("Enter Password:"))
if (p=="Avengers"):
    print("1.Bytes to Bits:")
    ch=int(input("Choose one option:"))
    if ch==1:
        Bytes=float(input("Enter the number of bytes:"))
        a=8
        Bits=(Bytes*a)
        print("After converting bytes to bits:",Bits)
else:
    print("Wrong Password",n)
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
ch=int(input("Choose one of the above options:"))
if ch==1:
    sum=0
    count=int(input("How many numbers do you want?:"))
    for i in range(count):
        num=float(input("Enter number:"))
        sum=num+sum
    print("Sum:",sum)
elif ch==2:
    difference=0
    count=int(input("How many numbers do you want?:"))
    for i in range(count):
        num=float(input("Enter number:"))
        difference=num-difference
    print("Difference:",difference)
elif ch==3:
    product=1
    count=int(input("How many numbers do you want?:"))
    for i in range(count):
        num=float(input("Enter number:"))
        product=num*product
    print("Product:",product)
elif ch==4:
    quotient=1
    count=int(input("How many numbers do you want?:"))
    for i in range(count):
        num=float(input("Enter number:"))
        quotient=num/quotient
    print("Quotient:",quotient)
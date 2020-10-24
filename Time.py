n=str(input("Enter your name:"))
p=str(input("Enter Password:"))
if (p=="Avengers"):
    num1=int(input("Enter an hour between 1 and 12:"))
    num2=int(input("Enter the number of hours ahead:"))
    answer=0
    answer=num1+num2
    if answer>12:
        answer=answer-12
    print("Answer:", answer,"O'clock")
else:
    print("Wrong Password",n)
n=str(input("Enter your name:"))
p=str(input("Enter Password:"))
if (p=="Avengers"):

    name=str(input("Enter your name:"))
    a=int(input("Enter the Total number of Marks in all exams:"))
    math=float(input("Enter your marks in Math:"))
    science=float(input("Enter your marks in Science:"))
    SST=float(input("Enter your marks in Social Science:"))
    english=float(input("Enter your marks in English:"))
    computer=float(input("Enter your marks in Computer:"))
    hindi=float(input("Enter your marks in Hindi:"))
    kannada=float(input("Enter your marks in Kannada:"))
    tm=math+science+SST+english+computer+hindi+kannada
    percentage=(tm/a)*100
    print("So,",name,"The Total percentage of your marks is:",percentage,"%")
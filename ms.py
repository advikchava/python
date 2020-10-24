print("1.Seconds to minutes")
print("2.Minutes to seconds")
ch=int(input("Choose one option:"))

if ch==1:
    num=int(input("Enter time in seconds:"))
    minutes=int(num/60)
    seconds=int(num%60)
    print("After the Seconds are converted to Minutes, the result is:",minutes,"Minutes", seconds,"Seconds")

elif ch==2:
    num=float(input("Enter time in minutes:"))
    seconds=int(num*60)
    print("After the Minutes are converted to Seconds, the result is:", seconds,"Seconds")

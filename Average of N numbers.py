print("-----------------------------------------")
name=input("Enter your Name: ")
pin=int(1234)
password=int(input("Enter pin number: "))

if password==pin:
    print("Access Granted")

    num=int(input("How many subjects: "))
    total=0
    x=num*100
    for i in range(num):
        numbers=int(input("Enter subject mark: "))
        total+=numbers
    print("Total =",total,"/",x)
    if total<=x:
        average=total/num
        print("Average =",average)
    else:
        print("👉 Your total is greater than",x)
        print("👺Try again")

    if average>=90 and average<=100:
        print("Hi",name,"your grade is 👑 𝐀")
    elif average>=80 and average<90:
        print("Hi",name,"your grade is 😃 𝐁")
    elif average>=70 and average<80:
        print("Hi",name,"your grade is 😏 𝐂")
    elif average>=60 and average<70:
        print("Hi",name,"your grade is 😌 𝐃")
    else:
        print("😶 Ouch! No grade!")
        print("😐 Do well in next exams!")
else:
    print("Access Denied")
print("-----------------------------------------")
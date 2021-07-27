num=int(input("How many subjects: "))
total=0

for i in range(num):
    numbers=int(input("Enter subject mark: "))
    total+=numbers
print("Total =",total,"out of 100")

average=total/num
print("Average =",average)

if average>=90 and average<=100:
    print("Grade = A")
elif average<=80 and average>90:
    print("Grade = B")
elif average<=70 and average>80:
    print("Grade = c")
elif average<=60 and average>70:
    print("Grade = D")
else:
    print("No grade!")
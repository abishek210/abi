list1 = []
num = input("How many numbers do you want to add: ")
num=int(num)
#print(type(num))
print(range(num))

#for y in range(num):
#print(y)

for y in range(num):
  try:
    numbers = int(input("Enter number (#%s) : " % (y+1)))
    list1.append(numbers)
  except:
    print("Invalid number!")
print("Sum of %s = %s " % (list1, sum(list1)))
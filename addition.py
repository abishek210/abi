list2 = []
num = input("How many numbers do you want to add: ")
num=int(num)
#print(type(num))
print(range(num))

#for y in range(num):
#print(y)

for y in range(num):
  try:
    numbers = int(input("Enter number #%s : " % (y+1)))
    list2.append(numbers)
  except:
    print("Invalid number!")
print("multiply of %s = %s " % (list2, multiply(list2)))
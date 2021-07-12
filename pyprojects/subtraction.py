name = []
num = input("how many numbers do you want to subtract: ")
num = int(num)
print(range(num))


for x in range(num):
 try:
  numbers = int(input("Enter number #%s : "% (x+1)))
  name.append(numbers)
 except:
  print("Invalid numbers")
print("Sub of %s = %s " % (name, sub(list)))

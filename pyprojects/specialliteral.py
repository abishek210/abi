foods="Available"
drinks="Available"
snacks=None

def menu(x) :
    if x=="Available" :
        print("Yes, you can have it")
    else:
        print("Stock Not available !!")
def my_line1():
 print("1.Foods")
def my_line2():
 print("2.Drinks")
def my_line3():
 print("3.snacks")    


cont="Y"
while (cont == "Y" or cont == "y"):
    my_line1()
    my_line2()        
    my_line3()

    choice = int(input("what do you want to have:  "))

    if choice==1:
        menu(foods)
    elif choice==2:
        menu(drinks)
    elif choice==3:
        menu(snacks)
    elif choice>3:
        print("Invalid option")
    cont = input("Do you want to continue (Yy/Nn)?:  ")



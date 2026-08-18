#Products Prices

Burger_and_chips = 49.66
Pizza = 99.99
Burger = 32.99
Chips = 27.50
Cool_drink = 10
Ice_cream = 5

#Program
def program():
 print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
 print("")
 print("   Welcome To The Cashier Program")
 print("")
 print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
 print("")
 print("Choose what the customer bought:  ")
 print("")
 print("1. Burger & Chips")
 print("2. Pizza")
 print("3. Burger Only")
 print("4. Chips Only")
 print("5. Cool Drink")
 print("6. Ice cream")
 print("")
 product= int(input("What did the customer buy?: "))
 print("")
 print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
 print("")

 if product == 1:
    price = float(input("How much did the customer pay for the Burger & Chips: "))
    change = float(price - Burger_and_chips)
    print("")
    print(f"The customers total is R{Burger_and_chips}")
    print(f"The customer paid R{price}")
    print(f"The customers change is R{change}")
    print("")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("")
    restart_program = str(input("While we are at it, would you like to serve another customer? (y/n): "))
    if restart_program == y:  
       program()
    elif restart_program == n:
       print("Thank you for using the Casier Service Program")      
 elif product == 2:
    price = float(input("How much did the customer pay for the Pizza: "))
    change = float(price - Pizza)
    print("")
    print(f"The customers total is R{Pizza}")
    print(f"The customer paid R{price}")
    print(f"The customers change is R{change}")
    print("")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
 elif product == 3:
    price = float(input("How much did the customer pay for the Burger: "))
    change = float(price - Burger)
    print("")
    print(f"The customers total is R{Burger}")
    print(f"The customer paid R{price}")
    print(f"The customers change is R{change}")
    print("")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
 elif product == 4:
    price = float(input("How much did the customer pay for the Chips: "))
    change = float(price - Chips)
    print("")
    print(f"The customers total is R{Chips}")
    print(f"The customer paid R{price}")
    print(f"The customers change is R{change}")
    print("")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
 elif product == 5:
    price = float(input("How much did the customer pay for the Cool Drink: "))
    change = float(price - Cool_drink)
    print("")
    print(f"The customers total is R{Cool_drink}")
    print(f"The customer paid R{price}")
    print(f"The customers change is R{change}")
    print("")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
 elif product == 6:
    price = float(input("How much did the customer pay for the Ice cream: "))
    change = float(price - Ice_cream)
    print("")
    print(f"The customers total is R{Ice_cream}")
    print(f"The customer paid R{price}")
    print(f"The customers change is R{change}")
    print("")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")   
 else:
    print("You have entered an invalid input, please choose the numbers from the Product list") 

program()                

    
    

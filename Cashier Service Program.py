#Products Prices

Burger_and_chips = 49.66
Pizza = 99.99
Burger = 32.99
Chips = 27.50
Cool_drink = 10
Ice_cream = 5

#Program

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

if product == 1:
    price = float(input("How much did the customer pay for the Burger & Chips: "))
    change = float(price - Burger_and_chips)
    print(f"The customers total is R{Burger_and_chips}")
    print(f"The customer paid R{price}")
    print(f"The customers change was R{change}")
    
    

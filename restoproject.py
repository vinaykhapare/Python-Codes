menu ={
    'pizza': 50,
    'burger': 40,
    'fries': 30,
    'coke': 20,
    'water': 10
    
}

#Greet
print("Welcome to the restaurant")
print("Pizza: 50\nBurger: 40\nFries: 30\nCoke: 20\nWater: 10")


#Order

order = []
while True:
    item = input("Enter the item you want to order or 'done' to finish: ")
    if item == 'done':
        break
    if item in menu:
        order.append(item)
        print("Added", item, "to the order")
        print("Current order:", order)
        print("Total cost:", sum(menu[item] for item in order))
        print()
    else:
        print("Invalid item. Please try again.")
        print()
print()
total_cost=sum(menu[item] for item in order)
print("Your Total Amount is:",total_cost)        
print("Thank You \nVisit Again !!!")


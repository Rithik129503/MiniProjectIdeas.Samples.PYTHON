#Project 1 [sample]
#Cafe menu

menu = {
    'tea':30,
    'coffee': 45,
    'french fries': 60,
    'veg pizza': 110,
    'veg salad': 80,
    'soft drinks':30,
    }
    
print("Welcome to Rithik Cafe!")
#Showing menu to the customer

print("tea: Rs30\ncoffee: Rs45\nfrench fries: Rs60\nveg pizza: Rs110\nveg salad: Rs80\nsoftdrinks: Rs30")

order_total = 0
#order ruppes of customer

#Taking order from the customer
item_1 =(input("Enter your order please ="))
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your selected item {item_1} is addded.")
else:
    print("ordered item {item_1} is not available yet!")
    
another_order = (input("Do you want anything else? (yes/no) "))
if another_order == "yes":
    item_2 = (input("Enter your order please = "))
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} is addded.")
    else:
        print("Order anything else in the menu please!")
        
print(f"The total amount of order is {order_total} to pay.")
print("Thankyou visit again.")

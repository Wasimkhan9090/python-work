menu = {
    "burger":65,
    "pizza":100,
    "cake": 60,
    "maggie":50,
    "coffee":45}
print("welcome to our python restaurent")
print(" burger : Rs65\npizza: Rs100\ncake: Rs60\nmaggie: Rs50\ncoffee: Rs45 ")
order_total = 0
item_1 = input("Enter the name of the item you want to order  = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"order item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order =="Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Item {item_2} is not available!")    
       
print(f"The total amount of items is to pay: {order_total}")

    


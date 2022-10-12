# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.
menu = ["Chicken Burger", "Beef Burger", "Veggie Burger", "Chips", "Chicken Wrap", "Veggie Wrap", "Coke", "Fanta", "Water"]
for i in menu:
    print(i)
#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
orders_list = []

order1 = input("Please make your First Order: ")

orders_list.append(order1)

order2 = input("Please make your Second Order: ")

orders_list.append(order2)

order3 = input("Please make your Third Order: ")

orders_list.append(order3)

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

for j in orders_list:
    print(j)
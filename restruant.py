#restraunt management system
menu={
    "pizza":250,
     "Burger":200,
     "momo":190,
     "Chowmein":150,
     "Corn dog":120
     }
print("----------Welcome to Python Restraunt----------")
cost=0
while True:
    print("What do you want to order?\n")
    choice=input("Food from menu:")
    if choice in menu:
        cost+=menu[choice]
    else:
        print("Sorry!!We are out of stock for such items!!")
    ch=input("Do you want to order some more(Y/N):").lower()
    if ch=='n':
        break
print("The total cost become\t",cost)


#inventory management system
inventory={
    "milk":{"price":50,"quantity":10},
    "bread":{"price":50,"quantity":20},
    "egg":{"price":35,"quantity":12}
}
cost=0
print("----------Welcome to Python Store----------")
while True:
    print("What do you want to order\n")
    choice=input("Enter your choice:").lower()
    if choice in inventory:
     if inventory[choice]["quantity"]>0:
      cost+=inventory[choice]["price"]
      inventory[choice]["quantity"]-=1
      ch=input("You want to order some more:(Y/N)")
      if ch=='n':
       break
print("Total cost is",cost)
print(inventory)
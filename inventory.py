# inventory.py
stuff = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }

def displayInventory(inventory):
    total_items=0
    for item in inventory:
        print(str(inventory[item])+''+item)
        total_items += inventory[item]
    print("Total number of items:"+str(total_items))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] +=1
    return inventory
inv = {'gold coin':42, 'rope': 1}
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)



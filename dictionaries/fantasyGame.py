equipment = {'rope': 1,
             'torch': 6,
             'gold coin': 42,
             'dagger': 1,
             'arrow': 12}

inv = {'gold coin': 42,
       'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    num_items = 0
    for i, n in inventory.items():
        print(str(n) + ' ' + str(i))
        num_items += n
    print('Total number of items: ' + str(num_items))

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] = inventory[addedItems[i]] + 1
        else:
            inventory.setdefault(addedItems[i], 1)
    return inventory

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)

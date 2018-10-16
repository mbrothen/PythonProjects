# inventory.py 
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def display_inventory(inventory): 
    print("Inventory:") 
    item_total = 0 
    for k, v in inventory.items():
         print(str(v) + ' ' + k) 
         item_total += v 
    print("Total number of items: " + str(item_total)) 
    
def addToInventory(inventory, addedItems):
	for i in addedItems:
		if inventory.get(i):
			inventory[i] += 1
		else:
			inventory[i] = 1
	return inventory

stuff = addToInventory(stuff, loot)
display_inventory(stuff) 
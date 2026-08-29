items = ["pencil", "Eraser" , "sharpener", "glue", "notebook"]
stock_counts = [12,0,8,5,3]


inventory = {item:count for item, count in zip(items,stock_counts)}
print("Full inventory:",inventory)


in_stock_items = [item for item in items if inventory[item]>0]
print("items in stock:",in_stock_items)


chosen_item = input("which item do you want to buy?")

if chosen_item not in inventory or inventory [chosen_item] == 0:
    print(chosen_item, "item out of stock,stopping the checker")
exit()


prices = [10,5,40,15,20]
markup = int(input("Enter the markup amount to enter every price"))


mark_up_prices = list(map(lambda p:p+markup,prices))
print(" mrk_up_prices",mark_up_prices)


item_index = items.index(chosen_item)
chosen_price = mark_up_prices[item_index]
print("price_of",chosen_item,"after_markup",chosen_price)

inventory [chosen_item] = inventory [chosen_item]-1
print(chosen_item,"purchased!Inventory chosen_item",inventory [chosen_item])



print("")
print("======SCHOOL STORE INVENTORY CHECKER======")
print("ITEM BROUGHT",chosen_item)
print("price paid",chosen_price)
print("update inventory:", inventory)
print("==================================================")
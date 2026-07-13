# ================================
#  SNACK STORE INVENTORY
#  File: snack-store-inventory.py
# ================================


# PART 1 — DATA TYPES
item_name = "Popcorn"       # str   — text
item_cost = 2.25            # float — decimal number
stock_count = 15            # int   — whole number
available = True            # bool  — availability status

print("Item:", item_name)
print("Cost: $", item_cost)
print("Items in Stock:", stock_count)
print("Available for Sale:", available)

print(type(item_name))
print(type(item_cost))
print(type(stock_count))
print(type(available))


# PART 2 — ARITHMETIC OPERATORS
inventory_value = item_cost * stock_count
print("Inventory Value: $", inventory_value)
print("Discounted Cost: $", item_cost - 0.50)
print("Stock After Restocking:", stock_count * 2)


# PART 3 — COMPARISON OPERATORS
print("Does the item cost less than $3?", item_cost < 3)
print("Are there more than 10 items?", stock_count > 10)
print("Is the item price exactly $2.25?", item_cost == 2.25)


# PART 4 — STRING OPERATIONS
store_name = "Snack" + " " + "Corner"
print("Store Name:", store_name)
print("Number of letters in item name:", len(item_name))
print("First letter of the item:", item_name[0])


# PART 5 — SWAPPING VALUES
cost_one = 2.25
cost_two = 3.50

print("Prices before swapping:", cost_one, "and", cost_two)

temporary_price = cost_one
cost_one = cost_two
cost_two = temporary_price

print("Prices after swapping:", cost_one, "and", cost_two)
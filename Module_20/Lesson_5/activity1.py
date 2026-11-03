# PART 1: Create a list of store products and their quantities
products = ["pencil", "eraser", "notebook", "sharpener", "glue"]
quantities = [12, 0, 8, 5, 3]

# PART 2: Combine products and quantities into a dictionary
store_inventory = {product: quantity for product, quantity in zip(products, quantities)}
print("Store Inventory:", store_inventory)

# PART 3: Find products that are available
available_products = [product for product in products if store_inventory[product] > 0]
print("Available Products:", available_products)

# PART 4: Ask the customer to select a product
selected_product = input("Enter the product you want to purchase: ")

# PART 5: Stop the program if the product is unavailable
if selected_product not in store_inventory or store_inventory[selected_product] == 0:
    print(selected_product, "is not available! Closing the checker.")
    exit()

# PART 6: Set product prices and ask for an extra amount
prices = [10, 5, 40, 15, 20]
extra_amount = int(input("Enter the extra amount to add to each price: "))

# PART 7: Add the extra amount to all prices using map()
updated_prices = list(map(lambda price: price + extra_amount, prices))
print("Updated Product Prices:", updated_prices)

# PART 8: Get the updated price of the selected product
product_index = products.index(selected_product)
final_price = updated_prices[product_index]
print("Updated price of", selected_product, ":", final_price)

# PART 9: Update the quantity after the purchase
store_inventory[selected_product] = store_inventory[selected_product] - 1
print(selected_product, "purchased successfully! Stock left:", store_inventory[selected_product])

# PART 10: Display the final store report
print("")
print("===== STORE INVENTORY REPORT =====")
print("Purchased Product:", selected_product)
print("Final Price:", final_price)
print("Remaining Inventory:", store_inventory)
print("==================================")
# Define a list of available items and their prices
items = {
    "A": 1.00,
    "B": 1.50,
    "C": 2.00
}

# Prompt the user to select an item
user_selection = input("Please select an item (A, B, or C): ")

# Validate the user's selection
if user_selection not in items:
    print("Invalid selection. Please select an item from the list.")
    exit()

# Get the price of the selected item
item_price = items[user_selection]

# Prompt the user to enter coins
coins = {
    "$0.25": 0,
    "$0.50": 0,
    "$1.00": 0
}

total_coins = 0

for coin in coins:
    coin_count = int(input("Enter the number of {} coins: ".format(coin)))
    coins[coin] = coin_count
    total_coins += coin_count * float(coin.replace("$", ""))

# Check if the user has paid enough money
if total_coins < item_price:
    print("Insufficient funds. Please insert more coins.")
    exit()

# Dispense the item
print("Thank you for your purchase. Your item has been dispensed.")

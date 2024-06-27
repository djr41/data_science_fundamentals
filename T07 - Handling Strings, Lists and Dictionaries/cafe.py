# ========= Task 7 - cafe.py =========
# Simple program to calculate the total value of stock at a cafe by
# defining a dictionary that contains stock and price data for each item on the menu.

# intialise the menu items
menu = ['eggs', 'bacon', 'mushrooms', 'tomatoes']

# create a dictionary for the stock levels using the menu items as keys
stock = { 'eggs':  24,
          'bacon': 21,
          'mushrooms': 30,
          'tomatoes': 62
         }

# create a dictionary for the price levels using the menu items as keys
price = { 'eggs':  1.6,
          'bacon': 2.1,
          'mushrooms': 0.8,
          'tomatoes': 0.7
         }

# initialise a variable to hold the total value
total_value=0

# loop over the menu items calculating item_value and add this to total_value
for items in menu:
    item_value=stock[items]*price[items]
    total_value=total_value+item_value

# print the reult in a user friendly format
print(f"The total value of the stock is £{total_value:.2f}")
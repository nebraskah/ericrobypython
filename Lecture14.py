"""
Simple Groceries
"""
import Lecture14Service as Service

items_to_purchase = {
    'Candy': 7,
    'Notebook': 15,
    'Paper': 8,
    'Coffee': 3,
    'Socks': 7
}

user_money_real = False
while not user_money_real:
    user_input = input('How much money do you have?: ').strip()
    if user_input.isdigit():
        user_money = int(user_input)
        user_money_real = True

items_price_added_to_cart = []

user_shopping = False

while not user_shopping:
    add_item_to_cart = input('What item would you like to purchase?: ').capitalize().strip()

    if add_item_to_cart in items_to_purchase:
        print(f'Item {add_item_to_cart} added to cart')
        items_price_added_to_cart.append(items_to_purchase.get(add_item_to_cart))
        print(f'You currently have {len(items_price_added_to_cart)} items in your cart')
    else:
        print(f'Item {add_item_to_cart} is not at this store')
    user_shopping = input('Checkout (Y/N?): ').lower().strip() == 'Y'.lower()
Service.purchased_items(user_money_arg=user_money, items=items_price_added_to_cart)
print('Volte Sempre!')



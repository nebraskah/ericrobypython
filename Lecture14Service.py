"""
Grocery App - Service Class
"""


def purchased_items(user_money_arg, items):
    items_total_cost = 0;
    for item in items:
        items_total_cost += item
    print(f'Total payable is EUR {items_total_cost} for {len(items)} items.')
    if items_total_cost <= user_money_arg:
        amount_left = user_money_arg - items_total_cost
        print(f'Amount Left: EUR {amount_left}')
    else:
        print('Poor you!')



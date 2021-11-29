header = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""

menu = {
    'Appetizers': ['Wings', 'Cookies', 'Spring rolls'],
    'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
    'Desserts': ['Ice Cream', 'Cake', 'Pie'],
    'Drinks': ['Coffee', 'Tea', 'Unicorn Tears'],
}

prompt = """
***********************************
** What would you like to order? **
***********************************
> """

def show_menu():
    for key, value in menu.items():
        print(key)
        print('-------')
        for item in value:
            print(item)
        print(' ')


print(header)
show_menu()

orders = {}

flag = True

while flag:
    new_order = str(input(prompt))

    if new_order == 'quit':
        flag = False
        print(f'You ordered: {orders}')

    if new_order == 'show order':
        print(orders)

    if new_order in orders:
        orders[new_order] += 1
        print(f'{orders[new_order]} orders of {new_order} added to your meal')
    else:
        for sublist in list(menu.values()):
            if new_order in sublist:
                orders[new_order] = 1
                print(f'1 order of {new_order} has been added to your meal')

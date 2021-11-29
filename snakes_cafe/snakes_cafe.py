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

prompt = """***********************************
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
new_order = str(input(prompt))

for sublist in list(menu.values()):
    if new_order in sublist:
        print(f'1 order of {new_order} has been added to your meal')

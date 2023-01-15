from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_info = CoffeeMaker()
coffee_menu = Menu()
menu_item = MenuItem
money_machine = MoneyMachine()

menu_choose = "on"

while menu_choose != "off":

    menu_choose = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()

    if menu_choose == "report":
        coffee_info.report()
        money_machine.report()

    elif coffee_menu.find_drink(menu_choose).name:
        coffee_select = coffee_menu.find_drink(menu_choose)
        sufficiency = coffee_info.is_resource_sufficient(coffee_select)

        if sufficiency == True:
            money_check = money_machine.make_payment(coffee_select.cost)

            if money_check == True:
                coffee_info.make_coffee(coffee_select)



#         if is_enough == True:
#             print("Please insert coins")
#             quarter = int(input("how many quarter?: "))
#             dimes = int(input("how many dimes?: "))
#             nickels = int(input("how many nickles?: "))
#             pennies = int(input("how many pennies?: "))

#             money = money_change(menu, coin, quarter, dimes, nickels, pennies)
#             total = round(money[0], 2)


#             if total >= MENU[menu]['cost']:
#                 left_coffee = make_coffee(menu, water, milk, coffee)

#                 coin = money[2]
#                 water = left_coffee[1]
#                 milk = left_coffee[2]
#                 coffee = left_coffee[3]
#                 print(f"Here is ${round(money[1], 2)} in change.")
#                 print(f"Here is your {left_coffee[0]} ☕️. Enjoy!")

#             else:
#                 print("Sorry that's not enough money. Money refunded")


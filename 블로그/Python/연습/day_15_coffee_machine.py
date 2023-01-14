MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

water, milk, coffee, coin = 300, 200, 100, 0

def is_sufficient(menu, water, milk, coffee):
    if water >= MENU[menu]["ingredients"]["water"] and coffee >= MENU[menu]["ingredients"]["coffee"]:
        if "milk" in MENU[menu]["ingredients"]:
            if milk >= MENU[menu]["ingredients"]["milk"]:
                return True
        else:
            return True
    else:
        if water < MENU[menu]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        if "milk" in MENU[menu]["ingredients"]:
            if milk < MENU[menu]["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")
        if coffee < MENU[menu]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        return False


def make_coffee(menu, water, milk, coffee):
    if is_sufficient(menu, water, milk, coffee) == True:
        water -= MENU[menu]["ingredients"]["water"]
        if "milk" in MENU[menu]["ingredients"]:
            milk -= MENU[menu]["ingredients"]["milk"]
        coffee -= MENU[menu]["ingredients"]["coffee"]
        return menu, water, milk, coffee


def money_change(menu, coin, quarter, dimes, nickels, pennies):
    quarter = quarter * 0.25
    dimes = dimes * 0.1
    nickels = nickels * 0.05
    pennies = pennies * 0.01

    total = quarter + dimes + nickels + pennies
    change = total - MENU[menu]["cost"]
    coin += MENU[menu]["cost"]

    return total, change, coin


menu = "on"

while menu != "off":

    menu = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if menu == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${coin}")

    elif menu == "espresso" or menu == "latte" or menu == "cappuccino":
        is_enough = is_sufficient(menu, water, milk, coffee)

        if is_enough == True:
            print("Please insert coins")
            quarter = int(input("how many quarter?: ")) 
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            
            money = money_change(menu, coin, quarter, dimes, nickels, pennies)
            total = round(money[0], 2)


            if total >= MENU[menu]['cost']:
                left_coffee = make_coffee(menu, water, milk, coffee)

                coin = money[2]
                water = left_coffee[1]
                milk = left_coffee[2]
                coffee = left_coffee[3]
                print(f"Here is ${round(money[1], 2)} in change.")
                print(f"Here is your {left_coffee[0]} ☕️. Enjoy!")
            
            else:
                print("Sorry that's not enough money. Money refunded")
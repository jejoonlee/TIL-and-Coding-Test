# Udemy : Python 커피 머신 프로젝트

> #### 3개 종류의 커피들이 주어진다
>
> #### 필요한 재료와 금액이 주어진다

- #### 유저는 어떤 커피를 마실지, 그리고 동전 얼마를 넣을지 입력을 한다

- #### 입력에 따라, 재료가 부족하든지, 금액이 부족하든지, if문을 넣었다

- #### 여기서 제일 집중했던 것은 함수를 만드는 것이었다

  - `is_sufficient` : 안에 재료가 적당히 있는지 확인하는 함수
  - `make_coffee`: `is_sufficient`가 True를 반환하면, 커피를 만드는 함수이다
  - `money_change`: 금액을 계산하는 함수이다

- #### 함수를 사용해서, 2개 이상의 변수를 반환했다

  - 튜블로 반환이 되어서, 인덱스를 통해, 내가 원하는 데이터를 활용했다



```python
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
```












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

income = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_enough(order_ingredients):
    """Returns True when order can be made and False if ingredients aren't enough"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Retuns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global income
        income += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

machine_is_on = True
# 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
while machine_is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if order == "off":
        print("Machine turned off. Bye!")
        machine_is_on = False
    # 3. Print report.
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
        print(f"Money: ${income}")
    # 4. Check resources sufficient?
    else:
        drink = MENU[order]
        if is_resource_enough(drink["ingredients"]):
            # 5. Process coins.
            payment = process_coins()
            # 6. Check transaction successful?
            is_transaction_successful(payment, drink["cost"])
            # 7. Make Coffee.
            make_coffee(order, drink["ingredients"])

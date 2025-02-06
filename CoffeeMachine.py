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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_sufficient(order_ingredients):
    """Checks if resources are sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there isn't enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total amount"""
    print("Please insert coins.")
    total = int(input("Quarters: ")) * 0.25
    total += int(input("Dimes: ")) * 0.1
    total += int(input("Nickels: ")) * 0.05
    total += int(input("Pennies: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    refund_amount = 0
    if money_received > drink_cost:
        refund_amount = money_received - drink_cost
    elif money_received < drink_cost:
        return -1
    return refund_amount

go_again = True
while go_again:
    choice = input("What would you like?(espresso/ latte/ cappuccino): ")
    if choice == 'off':
        go_again = False
    elif choice == 'report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${profit}")
    elif choice == 'add':
        adding_amount = 0
        for item in resources:
            adding_amount = int(input(f"{item}: "))
            resources[item] += adding_amount
    else:
        drink = MENU[choice]
        if resources_sufficient(drink['ingredients']):
            print(f"Cost: {MENU[choice]['cost']}")
            payment = process_coins()
            refund = is_transaction_successful(payment, drink['cost'])
            if refund == -1:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += drink['cost']
                print(f"Processing your drink\nMoney refunded: ${round(refund, 2)}")
                for item in drink['ingredients']:
                    resources[item] -= drink['ingredients'][item]
                print(f"Here's your {choice}🍵!")
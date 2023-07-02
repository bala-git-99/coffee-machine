MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

drink_names = {'espresso', 'latte', 'cappuccino', }

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# TODO 1. Take order by prompting the user
# TODO 2. If the user enters 'off', the code should be terminated
# TODO 3. Printing the report
# TODO 4. Check if the resources are sufficient
# TODO 5. Get the coins from the user and calculate the total amount
# TODO 6. Check whether the transaction is successful; compare the amount inserted with the amount required for the...
# drink chosen; If the amount is sufficient, add the amount in the resources. If it is not enough, stop the transaction,
# refund the money and prompt the user fresh for a new drink
# TODO 7. Make coffe if the transaction is successful; display the message aptly


def report():
    """This function will print the remaining resources in the machine as a report"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(drink_name):
    for resource in resources:
        if resource != "money" and MENU[drink_name]['ingredients'][resource] >= resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def take_order():
    """This function will take order by prompting the user"""
    choice_of_drink = input("What would you like? (espresso/latte/cappuccino): ")
    return choice_of_drink


def get_coins():
    inserted_coins = []
    print("Please insert coins.")
    for coin in coins:
        input_coin = int(input(f"how many {coin}?: "))
        input_coin = input_coin * coins[coin]
        inserted_coins.append(input_coin)
    return sum(inserted_coins)


def check_amount(total_amount, choice_of_drink):
    """This function will return the remaining amount in excess. If it isn't sufficient, it will return -1"""
    if total_amount < MENU[choice_of_drink]['cost']:
        return -1
    else:
        return total_amount - MENU[choice_of_drink]['cost']


def start_coffee_machine():
    choice_of_drink = take_order()
    resource_available = True
    if choice_of_drink == "off":
        # Terminate the code
        return False
    elif choice_of_drink == 'report':
        report()
        return True
    elif choice_of_drink not in drink_names or not bool(choice_of_drink):
        print("Please enter a valid option")
        return True
    else:
        resource_available = check_resources(choice_of_drink)
        if not resource_available:
            return True

    total_amount = get_coins()
    return_amount = check_amount(total_amount, choice_of_drink)
    if return_amount == -1:
        print("Sorry that's not enough money. Money refunded.")
        return True
    elif return_amount > 0:
        print(f"Here is ${return_amount} dollars in change.")

    if return_amount >= 0:
        resources["water"] = resources["water"] - MENU[choice_of_drink]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[choice_of_drink]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[choice_of_drink]["ingredients"]["coffee"]
        resources['money'] = resources['money'] + MENU[choice_of_drink]["cost"]

        print(f"Here is your {choice_of_drink}. Enjoy!")
        return True


start_machine = True

while start_machine:
    start_machine = start_coffee_machine()

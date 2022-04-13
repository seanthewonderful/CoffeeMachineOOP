from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


espresso = Menu().find_drink("espresso")
latte = Menu().find_drink("latte")
cappuccino = Menu().find_drink("cappuccino")
water = CoffeeMaker().resources["water"]
milk = CoffeeMaker().resources["milk"]
coffee = CoffeeMaker().resources["coffee"]

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True


while is_on:
    choice = input(f"What would you like? ({Menu().get_items()}): ")
    drink = Menu().find_drink(choice)
    # if choice == "espresso":
    #     if CoffeeMaker().is_resource_sufficient(espresso):
    #         if MoneyMachine().make_payment(espresso.cost):
    #             CoffeeMaker().make_coffee(espresso)
            
    # elif choice == "latte":
    #     CoffeeMaker().is_resource_sufficient(latte)
    #     if MoneyMachine().make_payment(latte.cost):
    #         CoffeeMaker().make_coffee(latte)
            
    # elif choice == "cappuccino":
    #     CoffeeMaker().is_resource_sufficient(cappuccino)
    #     if MoneyMachine().make_payment(cappuccino.cost):
    #         CoffeeMaker().make_coffee(cappuccino)
            
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        if CoffeeMaker().is_resource_sufficient(drink):
            if MoneyMachine().make_payment(drink.cost):
                CoffeeMaker().make_coffee(drink)
        
        

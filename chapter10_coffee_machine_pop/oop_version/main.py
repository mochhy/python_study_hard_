




menu = MENU()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
while is_on :
    choice = input(f"어떤 음료를 드시겠습니까? {menu.get_items()}>>>").lower()
    if choice == "off" :
        is_on = False
        print("자판기가 종료되었습니다.")
    elif choice == "report" :
         coffe_maker.report()
         money_machinereport()

    else :
        drink = menu.find_drink
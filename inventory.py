file1 = 'inventory.txt'


def menu():
    print('\n*** MAIN MENU ***\n')
    print('[1] - Register new product')
    print('[2] - Input or remove quantity')
    print('[3] - General report')
    print('[4] - Unavailable products report')
    print('[5] - Exit system\n')
    option = input('Chose an option: ')
    while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
        option = input('Please enter a valid value: ')
    if option == '1':
        return register()
    elif option == '2':
        return quantity()
    elif option == '3':
        return general_report()
    elif option == '4':
        return unavailable()
    elif option == '5':
        print('\n*** End of execution ***\n')


def register():
    with open(file1, 'a+', encoding='UTF-8') as file:
        print('\n*** INSERT NEW PRODUCT ***\n')

        while True:

            code = input('Product code: ')
            while len(code) == 0 or len(code) > 6:
                code = input('Please enter a valid code (up to 6 characters): ')
            while content(code) is True:
                code = input('Code already registered, please try a new one: ')

            prod = input('Product name: ')
            while len(prod) == 0 or len(prod) > 20:
                prod = input('Please enter a valid product (up to 20 characters): ')
            while content(prod) is True:
                prod = input('Product already registered, please try a new one: ')

            try:
                quant = int(input('Quantity: '))
            except ValueError:
                print('Invalid value')
                break

            file.write(f'{code} ')
            file.write(f'{prod} ')
            file.write(f'{quant}\n')

            option = input('Register another product? (y/n): ')
            while option.lower() != 'y' and option.lower() != 'n':
                option = input('Please type only "y" or "n": ')
            if option == 'n':
                print('\nProduct(s) registered sussesfully!')
                break

        print('\n[0] - Return to main menu')
        print('[1] - Exit system')
        option = input('\nChose an option: ')
        while option != '0' and option != '1':
            option = int(input('Please enter a valid value: '))
        if option == '0':
            return menu()
        elif option == '1':
            print('\n*** End of execution ***\n')


def quantity():

    lst = dic()
    print('\n*** INPUT OR REMOVE QUANTITY ***\n')
    prod = input('Product: ')
    if content(prod) is False:
        print('\nProduct not found\n')
        print('[0] - General report')
        print('[1] - Exit system')
        option = input('\nChose an option: ')
        while option != '0' and option != '1':
            option = int(input('Please enter a valid value: '))
        if option == '0':
            return general_report()
        elif option == '1':
            print('\n*** End of execution ***\n')
    else:
        try:
            quant = int(input('Please enter the quantity (include " - " to remove): '))
            for i in range(len(lst)):
                if lst[i]['product'] == prod:
                    lst[i]['quantity'] += quant
                    print(f"\nNew quantity of {lst[i]['product']} = {lst[i]['quantity']}")

            with open(file1, 'w', encoding='UTF-8') as file:
                file.truncate(0)
                for i in range(len(lst)):
                    file.write(f"{lst[i]['code']} {lst[i]['product']} {lst[i]['quantity']}\n")

            return menu()

        except ValueError:
            print('\nInvalid value')
            print('\n[0] - Return to main menu')
            print('[1] - Exit system')
            option = input('\nChose an option: ')
            while option != '0' and option != '1':
                option = int(input('Please enter a valid value: '))
            if option == '0':
                return menu()
            elif option == '1':
                print('\n*** End of execution ***\n')


def content(word):
    with open(file1, mode='r', encoding='UTF-8') as file:
        file.seek(0)
        lst = (file.read()).split()
        if word in lst:
            return True
        else:
            return False


def dic():
    with open(file1, mode='r+', encoding='UTF-8') as file:
        file.seek(0)
        lst = (file.read()).split()
        new_lst = []
        for i in range(0, len(lst) - 2, 3):
            di = {}
            key = 'code'
            value = lst[i]
            di.update({key: value})
            key = 'product'
            value = lst[i + 1]
            di.update({key: value})
            key = 'quantity'
            value = int(lst[i + 2])
            di.update({key: value})
            new_lst.append(di)
        return new_lst


def general_report():
    lst = dic()
    print('\n*** GENERAL REPORT ***\n')
    print('Code | Product | Quantity\n')
    for i in range(len(lst)):
        print(f"{lst[i]['code']} | {lst[i]['product'].upper()} | {lst[i]['quantity']}")
    input('\nPress ENTER for the main menu: ')
    return menu()


def unavailable():
    lst = dic()
    count = 0
    print('\n*** UNAVAILABLE PRODUCTS REPORT ***\n')
    for i in range(len(lst)):
        if lst[i]['quantity'] == 0:
            print(f"{lst[i]['product'].upper()}\n")
            count += 1
    if count == 0:
        print('No currently unavailable products')
    else:
        print(f'{count} product(s) unavailable')
    input('\nPress ENTER for the main menu: ')
    return menu()


menu()

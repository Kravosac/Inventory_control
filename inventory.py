file1 = 'inventory.txt'


def content(word):
    """
    This function reads the file and turns it into a list, then check if the
    parameter 'word' is in this list.
    """
    with open(file1, mode='r', encoding='UTF-8') as file:
        file.seek(0)
        lst = (file.read()).split()
        if word in lst:
            return True
        else:
            return False


def dic():
    """
    This function reads the file and turns it into a list with dictionaries inside.
    Each dictionary has 3 values: code, product and quantity. It is used inside other
    functions to easily find some key values.
    """
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


def menu():
    """
    This is the main menu. The other functions usually return this one after process themselves.
    """
    print('\n[1] - Register new product')
    print('[2] - Add or remove quantity')
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
    """
    This is the function to register a new product, with 3 key information: code,
    product and quantity. It checks if the code and product already exists in the
    current list, which means that they are already registered. The new data are
    appended in the end of the file.
    """
    with open(file1, 'a+', encoding='UTF-8') as file:
        print('\n*** INSERT NEW PRODUCT ***\n')

        while True:

            code = input('Product code: ')
            while content(code) is True:
                code = input('Code already registered, please try a new one: ')
                while len(code) == 0 or len(code) > 6:
                    code = input('Please enter a valid code (up to 6 characters): ')
            while len(code) == 0 or len(code) > 6:
                code = input('Please enter a valid code (up to 6 characters): ')

            prod = input('Product name: ')
            while content(prod) is True:
                prod = input('Product already registered, please try a new one: ')
                while len(prod) == 0 or len(prod) > 20:
                    prod = input('Please enter a valid product (up to 20 characters): ')
            while len(prod) == 0 or len(prod) > 20:
                prod = input('Please enter a valid product (up to 20 characters): ')

            try:
                quant = int(input('Quantity: '))
            except ValueError:
                print('Invalid value')
                return menu()

            file.write(f'{code} ')
            file.write(f'{prod} ')
            file.write(f'{quant}\n')

            option = input('Register another product? (y/n): ')
            while option.lower() != 'y' and option.lower() != 'n':
                option = input('Please type only "y" or "n": ')
            if option == 'n':
                print('\nProduct(s) registered sussesfully!')
                break

    return menu()


def quantity():
    """
    With this function the user can add or remove quantity of an existing product.
    The current data is erased from the file and the updated data will be written in it.
    If the product doesn't exist, the function returns a 'Product not found' message.
    """
    lst = dic()
    print('\n*** ADD OR REMOVE QUANTITY ***\n')
    prod = input('Product: ')
    if content(prod) is False:
        print('\nProduct not found')
        return menu()
    else:
        try:
            quant = int(input('Please enter the quantity (include " - " to remove): '))
            for i in range(len(lst)):
                if lst[i]['product'] == prod:
                    lst[i]['quantity'] += quant
                    if lst[i]['quantity'] < 0:
                        print(f'\nNot enough {prod.upper()} available. Current quantity = '
                              f'{lst[i]["quantity"] - quant}')
                        lst[i]["quantity"] -= quant
                        return menu()
                    else:
                        print(f"\nNew quantity of {lst[i]['product']} = {lst[i]['quantity']}")

            with open(file1, 'w', encoding='UTF-8') as file:
                file.truncate(0)
                for i in range(len(lst)):
                    file.write(f"{lst[i]['code']} {lst[i]['product']} {lst[i]['quantity']}\n")

        except ValueError:
            print('\nInvalid value')

    return menu()


def general_report():
    """
    This function checks the dictionary (which contains the current file data) and prints
    all the information in the screen.
    """
    lst = dic()
    print('\n*** GENERAL REPORT ***\n')
    print('Code | Product | Quantity\n')
    for i in range(len(lst)):
        c = lst[i]['code'] + " " * (6 - len(lst[i]['code']))
        p = lst[i]['product'] + " " * (20 - len(lst[i]['product']))
        q = lst[i]['quantity']
        print(f"{c} | {p.upper()} | {q}")

    return menu()


def unavailable():
    """
    This function checks the dictionary (which contains the current file data) and prints
    all the unavailable products (quantity = 0) in the screen.
    """
    lst = dic()
    count = 0
    print('\n*** UNAVAILABLE PRODUCTS REPORT ***\n')
    for i in range(len(lst)):
        if lst[i]['quantity'] == 0:
            print(f"{lst[i]['product'].upper()}")
            count += 1
    if count == 0:
        print('No currently unavailable products')
    else:
        print(f'\n{count} product(s) unavailable')

    return menu()


print('\n*** INVENTORY CONTROL ***')

menu()

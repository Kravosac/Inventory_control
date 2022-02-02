
file1 = 'inventory.txt'


def menu():
    print('\n*** OPTIONS MENU ***\n')
    print('[1] - Register new product')
    print('[2] - Input or remove quantity')
    print('[3] - General report')
    print('[4] - Unavailable products report')
    print('[5] - Exit system\n')
    option = int(input('Chose an option: '))
    if option == 1:
        return register()
    elif option == 2:
        return quantity()
    elif option == 3:
        return general_report()
    elif option == 4:
        return unavailable()
    elif option == 5:
        print('\n*** End of execution ***\n')


def register():

    with open(file1, 'a+', encoding='UTF-8') as file:
        print('\n*** INSERT NEW PRODUCT ***\n')

        while True:

            code = input('Product code: ')
            while content(code) is True:
                code = input('Code already registered, please try a new one: ')
            file.write(f'{code} ')

            prod = input('Product name: ')
            while content(prod) is True:
                prod = input('Product already registered, please try a new one: ')
            file.write(f'{prod} ')

            quant = int(input('Quantity: '))
            file.write(f'{quant}\n')

            option = input('Register another product? (y/n): ')
            if option == 'n':
                print('\nProduct(s) registered sussesfully')
                break

    return menu()


def quantity():

    with open(file1, 'w+', encoding='UTF-8') as file:
        file.seek(0)
        lst = (file.read()).split()
        print(lst)
        print('\n*** INPUT OR REMOVE QUANTITY ***\n')

        prod = input('Product: ')
        quant = int(input('Please enter the quantity (include " - " to remove): '))
        for i in range(len(lst)):
            if lst[i] == prod:
                file.write(f'{lst[i]} ')
                file.write(str(int(lst[i+1]) + int(quant)))
                i += 1
            else:
                file.write(f'{lst[i]} ')


def content(word):
    with open(file1, mode='r', encoding='UTF-8') as file:
        file.seek(0)
        lst = (file.read()).split()
        if word in lst:
            return True
        else:
            return False


def dic():
    with open(file1, mode='r', encoding='UTF-8') as file:
        file.seek(0)
        lst = (file.read()).split()
        new_lst = []
        for i in range(0, len(lst)-2, 3):
            di = {}
            key = 'code'
            value = lst[i]
            di.update({key: value})
            key = 'product'
            value = lst[i+1]
            di.update({key: value})
            key = 'quantity'
            value = lst[i+2]
            di.update({key: value})
            new_lst.append(di)
        return new_lst


def general_report():
    lst = dic()
    print('\n*** GENERAL REPORT ***\n')
    print('Code | Product | Quantity\n')
    for i in range(len(lst)):
        print(f"{lst[i]['code']} | {lst[i]['product']} | {lst[i]['quantity']}")
    input('\nPress any key for the main menu: ')
    return menu()


def unavailable():
    lst = dic()
    count = 0
    print('\n*** UNAVAILABLE PRODUCTS REPORT ***\n')
    for i in range(len(lst)):
        if lst[i]['quantity'] == '0':
            print(f"{lst[i]['product']}\n")
            count += 1
    if count == 0:
        print('No currently unavailable products')
    else:
        print(f'{count} product(s) unavailable')
    input('\nPress any key for the main menu: ')
    return menu()


menu()


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
    elif option == 5:
        print('\n*** End of execution ***\n')


def register():

    with open(file1, 'a+', encoding='UTF-8') as file:
        print('\n*** INSERT NEW PRODUCT ***\n')

        while True:

            code = input('Product code: ')
            while code in content(file):
                code = input('Code already registered, please try a new one: ')
            file.write(f'{code} ')

            prod = input('Product name: ')
            while prod in content(file):
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

    with open(file1, 'a+', encoding='UTF-8') as file:
        print('*** INPUT OR REMOVE QUANTITY ***')

        prod = input('Product: ')
        while prod not in content(file):
            prod = input('Product not found. Please enter a valid product: ')

        quant = int(input('Please enter the quantity (include " - " for remove): '))


def content(file):
    with open(file1, mode='a+', encoding='UTF-8') as file:
        file.seek(0)
        return (file.read()).split()




menu()
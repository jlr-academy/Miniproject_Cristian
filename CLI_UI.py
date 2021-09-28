from os import system
from io import UnsupportedOperation
from os_checker import clear_command

clear_command = clear_command()

class interface():
    def __init__(self):
        while True:
            system(clear_command)
            print('Main menu:\n'\
                '[0] Quit\n'\
                '[1] Product menu\n')
            
            user_input = self.check_if_input_is_a_menu_option([0, 1])

            if user_input == -1:
                print('Inappropriate input. Please input a pozitive single digit number, as per the menu\n')
            elif user_input == 0:
                exit()
            elif user_input == 1:
                system(clear_command)
                self.product_menu()

    def check_if_input_is_a_menu_option(self, choices):
        try:
            user_input = int(input("Please select a choice: "))
            print('')
            if user_input not in(choices):
                return -1
            return user_input
        except:
            return -1
    
    def write_to_file(self, file_content):
        f = open('List_of_products.txt', 'w')
        if len(file_content) > 0:
            f.write(file_content[0])
            for x in range(1, len(file_content)):
                f.write('\n' + file_content[x])
        f.close()
        return 1
    
    def check_if_file_exists(self):
        try:
            f = open('List_of_products.txt', 'r+')
            file_content = [x.replace('\n','') for x in f.readlines()]
            f.close()
            return file_content
        except (NameError, FileNotFoundError):
            return False

    def product_menu(self):
        while True:
            print('Products menu:\n'\
            '[0] Return to main menu\n'\
            '[1] Print products list\n'\
            '[2] Add new product\n'\
            '[3] Amend existing product\n'\
            '[4] Delete product\n'\
            '[5] Search products\n')
            
            user_input = self.check_if_input_is_a_menu_option([0, 1, 2, 3, 4, 5])

            if user_input == -1:
                system(clear_command)
                print('Inappropriate input. Please input a pozitive single digit number, as per the menu\n')
            elif user_input == 0:
                return
            elif user_input == 1:
                file_content = self.check_if_file_exists()
                if file_content:
                    system(clear_command)
                    print('List of products currently in the list:\n')
                    for x in file_content:
                        print(x)
                    print('')
                elif file_content == False or len(file_content) == 0:
                    system(clear_command)
                    print('The product list is empty\n')
            elif user_input == 2:
                product_to_add = input("Please provide product to add: ").lower()
                print('')
                file_content = self.check_if_file_exists()
                if file_content == False:
                    f = open('List_of_products.txt', 'a')
                    f.write(product_to_add)
                    f.close()
                    system(clear_command)
                    print('Product added succesfully.\n')
                elif product_to_add not in file_content:
                    f = open('List_of_products.txt', 'a')
                    if len(file_content) != 0:
                        f.write('\n')
                    f.write(product_to_add)
                    f.close()
                    system(clear_command)
                    print('Product added succesfully.\n')
                else:
                    system(clear_command)
                    print('Product already exists.\n')
            elif user_input == 3:
                product_to_replace = input("Please enter the name of the product you wish to change: ").lower()
                print('')
                new_product = input("Please enter the name of the new product: ").lower()
                print('')
                file_content = self.check_if_file_exists()
                if file_content:
                    try:
                        file_content.index(product_to_replace)
                    except ValueError:
                        system(clear_command)
                        print('The item you have inputted is not in the list.\n')
                        self.product_menu()
                        return
                    file_content[file_content.index(product_to_replace)] = new_product
                    status =  self.write_to_file(file_content)
                    if status == 1:
                        system(clear_command)
                        print(f'Product {product_to_replace} has been replaced with product {new_product}.\n')
                elif file_content == False or len(file_content) == 0:
                    system(clear_command)
                    print('The product list is empty\n')
            elif user_input == 4:
                product_to_delete = input("Please enter the name of the product to delete: ").lower()
                print('')
                file_content = self.check_if_file_exists()
                if file_content:
                    try:
                        file_content.index(product_to_delete)
                    except ValueError:
                        system(clear_command)
                        print('The item you have inputted is not in the list.\n')
                        return -1
                    file_content.remove(product_to_delete)
                    status = self.write_to_file(file_content)
                    if status == 1:
                        system(clear_command)
                        print(f'Product {product_to_delete} has been deleted.\n')
                elif file_content == False or len(file_content) == 0:
                    system(clear_command)
                    print('The product list is empty\n')
            elif user_input == 5:
                product_to_search = input("Please enter the name of the product to search for: ").lower()
                print('')
                file_content = self.check_if_file_exists()
                if file_content:
                    system(clear_command)
                    print(f'The following results have been found of keywork {product_to_search}:\n')
                    for product in file_content:
                        if product_to_search in product:
                            print(product)
                    print("")
                elif file_content == False or len(file_content) == 0:
                    system(clear_command)
                    print('The product list is empty\n')

test = interface()
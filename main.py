from os import system
from os_checker import clear_command
from products import products_menu
from auxiliary_functions import check_if_input_is_a_menu_option
from couriers import couriers_menu

clear_command = clear_command()

def main_app_start():
    while True:
        system(clear_command)
        print('Main menu:\n'\
            '[0] Quit\n'\
            '[1] Product menu\n'
            '[2] Couriers menu\n')
        
        user_input = check_if_input_is_a_menu_option([0, 1, 2])

        if user_input == -1:
            print('Inappropriate input. Please input a pozitive single digit number, as per the menu\n')
        elif user_input == 0:
            exit()
        elif user_input == 1:
            system(clear_command)
            products_menu(clear_command)
        elif user_input == 1:
            system(clear_command)
            couriers_menu(clear_command)

main_app_start()
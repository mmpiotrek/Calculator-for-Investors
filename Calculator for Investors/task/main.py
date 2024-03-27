# write your code here
import sqlite3
import display_menu


def crud_menu():
    while True:
        display_menu.display_crud_menu()
        user_option = input("Enter an option: ")
        if user_option == '0':
            print("Not implemented!")
            break
        elif user_option == '1':
            print("Not implemented!")
            break
        elif user_option == '2':
            print("Not implemented!")
            break
        elif user_option == '3':
            print("Not implemented!")
            break
        elif user_option == '4':
            print("Not implemented!")
            break
        elif user_option == '5':
            print("Not implemented!")
            break
        else:
            print("Invalid option!")


def top_ten_menu():
    while True:
        display_menu.display_top_ten_menu()
        user_option = input("Enter an option: ")
        if user_option == '0':
            print("Not implemented!")
            break
        elif user_option == '1':
            print("Not implemented!")
            break
        elif user_option == '2':
            print("Not implemented!")
            break
        elif user_option == '3':
            print("Not implemented!")
            break
        else:
            print("Invalid option!")

def main_menu():
    while True:
        display_menu.display_main_menu()
        user_option = input("Enter an option: ")
        if user_option == '0':
            print("Have a nice day!")
            break
        elif user_option == '1':
            crud_menu()
        elif user_option == '2':
            top_ten_menu()
        else:
            print("Invalid option!")


def main():
    main_menu()


if __name__ == '__main__':
    main()

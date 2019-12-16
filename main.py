import os

from registration import Registration
from login import Login


def login():
    """ redirect to login page"""
    login_page = Login()
    login_page.login_main_page()


def registration():
    """Register the new user"""
    registration_page = Registration()
    registration_page.registration_main_page()


if __name__ == '__main__':
    ch = ''

    while ch != 3:
        os.system('clear')
        print "\t\t\t\t\t\t\t***** MAIN MENU *****\n\n\n"
        print "\n\t1. LOGIN \t\t\t\t\t2. REGISTER NEW USER\t\t\t\t\t\t3. EXIT\n"
        try:
            ch = str(raw_input('\n\n\t\t\t\t\tENTER YOUR RESPONSE :- '))
            if ch == '1':
                login()
            elif ch == '2':
                registration()
                continue
            elif ch == '3':
                print("\tThank You !! Visit Again")
                break
            else:
                print("WRONG CHOICE")
            os.system('clear')
            continue

        except NameError:
            print("\n\tSelect Your Option between 1 to 3")
            ch = str(raw_input("\t\tEnter your choice : "))
        except SyntaxError:
            print("Select Your Option (1-3)")
            ch = str(raw_input("\tEnter your choice : "))


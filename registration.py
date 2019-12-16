import os
from base import Base
from verify import Verify
import pandas as pd


class Registration(object):

    def __init__(self):
        """Init."""
        os.system('clear')
        self.base = Base()
        self.verify = Verify()

    def print_details(self, data_list):
        """Printing details of new account"""
        os.system('clear')
        print("\t\t:::::: ACCOUNT DETAILS ::::::\n\n")
        print("\t\tACCOUNT ID: " + data_list[1])
        print("\n\t\tACCOUNT BALANCE: " + data_list[3])
        print("\n\t\tFULL NAME: " + data_list[10])
        print("\n\t\tIFSC CODE: " + data_list[11])
        print("\n\t\tMOBILE NUMBER: " + data_list[12])
        print("\n\t\tADDRESS: " + data_list[2])
        print("\n\t\tAADHAAR CARD NUMBER: " + data_list[0])
        print("\n\t\tCREDIT CARD NUMBER: " + data_list[4])
        print("\n\t\tCREDIT CARD PIN: " + data_list[5])
        print("\n\t\tCREDIT CARD CVV: " + data_list[6])
        print("\n\t\tDEBIT CARD NUMBER: " + data_list[7])
        print("\n\t\tDEBIT CARD PIN: " + data_list[8])
        print("\n\t\tDEBIT CARD CVV: " + data_list[9] + "\n")

    def write(self, data_list):
        """Writing data to the csv file."""

        data = {
            'aadhaar_card': data_list[0],
            'account_id': data_list[1],
            'address': data_list[2],
            'balance': data_list[3],
            'c_number': data_list[4],
            'c_pin': data_list[5],
            'c_cvv': data_list[6],
            'd_number': data_list[7],
            'd_pin': data_list[8],
            'd_cvv': data_list[9],
            'full_name': data_list[10],
            'ifsc_code': data_list[11],
            'mobile_number': data_list[12],
        }

        data_frame = pd.DataFrame(data, index=[0])
        self.base.write_data(data_frame, self.base.ACCOUNT_INFO_FILE, self.base.ACCOUNT_COLUMN_NAMES)
        print("\n\t\t***** Account Creation successful *****\n")
        print " ***** WELCOME TO NOBANK *****"

    def registration_main_page(self):
        """Adding the new user"""

        while True:
            os.system('clear')
            print("\t\t\t\t\t\t\t\t***** REGISTRATION MENU *****\n\n\n")
            print("\t\t\t\t\t\t\t\t1. REGISTRATION\n")
            print("\t\t\t\t\t\t\t\t2. EXIT\n")
            ch = str(raw_input('\tEnter your response:- '))
            try:
                if ch == '1':
                    full_name = self.verify.full_name()
                    aadhaar_card = self.verify.aadhaar()
                    address = str(raw_input("\tEnter your address : "))
                    mobile_number = self.verify.mobile_number()
                    os.system('clear')
                    print("\t\t\t\t\t\t\t\t***** PLEASE VERIFY YOUR DETAILS *****\n")
                    print("\n\tFULL NAME :-  " + full_name)
                    print("\n\tAADHAAR CARD NUMBER :-  " + aadhaar_card)
                    print("\n\tADDRESS :-  " + address)
                    print("\n\tMOBILE NUMBER :-  " + str(mobile_number))

                    ch_verify = str(raw_input("\n\n\tPress 1 to update the details"
                                              "\n\tPress 2 to continue"
                                              "\n\tChoose your option :- "))
                    if ch_verify == '1':
                        continue
                    if ch_verify == '2':
                        balance = '0'
                        ifsc_code = "ABCD1234567"
                        account_id = self.base.random_generator(16)
                        d_number = self.base.random_generator(16)
                        d_pin = self.base.random_generator(4)
                        d_cvv = self.base.random_generator(3)
                        c_number = self.base.random_generator(16)
                        c_pin = self.base.random_generator(4)
                        c_cvv = self.base.random_generator(3)

                        data_list = [aadhaar_card, account_id, address, balance, c_number, c_pin, c_cvv, d_number,
                                     d_pin, d_cvv, full_name, ifsc_code, mobile_number]
                        self.print_details(data_list)
                        self.write(data_list)

                        user_char = str(raw_input("\n\t\tPRESS 1 FOR MAIN PAIGE"
                                                  "\n\t\tPRESS 2 FOR REGISTRATION PAGE"
                                                  "\n\t\tChoose your option :- "))
                        if user_char == '1':
                            break
                        if user_char == '2':
                            continue
                    break

                elif ch == '2':
                    print("\t\tThank you !! Visit again")
                    break
                else:
                    print("Invalid choice")
                os.system('clear')
            except Exception:
                print("Select Your Option (1-2)")
                ch = str(raw_input("\nEnter your choice : "))

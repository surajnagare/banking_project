from base import Base
import os
import pandas as pd


class Verify(object):

    def __init__(self):
        """Init."""
        # os.system('clear')
        self.base = Base()

    def aadhaar(self):
        """Aadhar number from user.

        :return aadhaar_card_number: String, aadhaar card number
        """
        while True:
            aadhaar_card_number = str(raw_input("\t\t\t\t\t\t\t\tEnter Aadhaar Card number : "))
            if self.base.verify_aadhaar_card_number(aadhaar_card_number):
                return aadhaar_card_number
            else:
                print("\n\t\t**Note**\n\t\tPlease Enter 16 digit Aadhaar card number.\n")
                continue

    def full_name(self):
        """full_name of the user.

        :return: String, full_name
        """
        while True:
            full_name = str(raw_input("\t\t\t\t\t\t\t\tEnter Full Name : "))
            if self.base.verify_full_name(full_name):
                return full_name
            else:
                print("\n\t\t**Note**\n\t\tPlease Enter Correct Name\n")
                continue

    def beneficiary_account_id(self):
        """beneficiary account id of the user

        :return: String, account id
        """
        while True:
            beneficiary_account_id = str(raw_input('\t\t\t\t\t\t\t\tEnter 16 digit beneficiary account id :- '))
            if self.base.verify_account_number(beneficiary_account_id):
                return beneficiary_account_id
            else:
                print("\n\t\t**Note**\n\t\tPlease Enter correct 16 digit Account number.\n")

    def ifsc_code(self):
        """ifsc code from the user.

        :return: String, ifsc code
        """
        while True:
            ifsc_code = str(raw_input("\t\t\t\t\t\t\t\tEnter IFSC code :- "))
            if self.base.verify_ifsc_number(ifsc_code):
                return ifsc_code
            else:
                print("\n\t\t**Note**\n\t\tPlease Enter correct IFSC code (eg;- ABCD1234567)\n")
                continue

    def mobile_number(self):
        """Get the correct mobile number from user.

        :return: String, full_name
        """
        while True:
            mob_number = str(raw_input("\t\t\t\t\t\t\t\tEnter 10 digit Mobile Number : "))
            if self.base.verify_mobile_number(mob_number):
                return mob_number
            else:
                print("\n\t\t**Note**\n\t\tPlease Enter 10 digit mobile number (should be digit)\n")
                continue

    def pin_number(self):
        """Get the correct mobile number from user.

        :return: String, full_name
        """
        while True:
            pin_number = str(raw_input("\t\t\t\t\t\t\t\tEnter 4 Digit For Pin Number : "))
            if self.base.verify_pin_number(pin_number):
                return pin_number
            else:
                print"\n\t\t**Note** Please Enter 4  Digit Pin Number (should be digit) "
                continue

    @staticmethod
    def publish(account_data, display_name, column_name):
        """print the card details on the screen for the user.
        :param account_data: dictionary having account data.
        :param display_name: list having print statements .
        :param column_name: list having column name.
        """
        for (d_name, c_name) in zip(display_name, column_name):
            print "\t\t\t\t\t" + d_name + " :- " + account_data[c_name]
        print '\n'

    def duplicate(self, data_frame, filename, column_name):
        """removing the duplicates out of the file."""
        self.base.write_data(data_frame, filename, column_name)
        self.base.remove_duplicate(filename, column_name)

    def raise_error(self):
        raise ValueError

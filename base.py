import random
import math
import re
import pandas as pd


class Base(object):
    """Base file where we verify all the fields and are being used in other files."""

    ACCOUNT_INFO_FILE = '/home/nineleaps/github/banking_project/account_info.csv'
    ACCOUNT_COLUMN_NAMES = ["aadhaar_card", "account_id", "address", "balance", "c_number", "c_pin",
                                      "c_cvv", "d_number", "d_pin", "d_cvv", "full_name", "ifsc_code", "mobile_number"]

    BENEFICIARY_INFO_FILE = '/home/nineleaps/github/banking_project/beneficiary_info.csv'
    BENEFICIARY_COLUMN_NAMES = ["u_account_id", "b_account_id", "full_name", "ifsc_code", "mobile_number"]

    def __init__(self):
        """Init."""
        pass

    def random_generator(self, power):
        """Get random number based on power

        :params power: int
        :return string: random number of length power
        """
        return str(random.randrange(1*pow(10, power-1), 1*pow(10, power)))

    def verify_full_name(self, full_name):
        """Verify full name.

        :param full_name: String, full name
        :return Boolean: True, False
        """
        return True if re.search(r'[0-9@_!#$%^&*()<>?/\|}{~:]', full_name) is None else False

    def verify_mobile_number(self, mob_number):
        """Verify mobile number.

        :param mob_number: String, mobile number
        :return Boolean: True, False
        """
        return True if len(mob_number) == 10 and mob_number.isdigit() else False

    def verify_ifsc_number(self, ifsc):
        """Verify ifsc code.

        :param ifsc: String, ifsc code
        :return Boolean: True, False
        """
        return True if len(ifsc) == 11 and re.match(r'[A-Za-z]{4}[0-9]{7}$', ifsc) else False

    def verify_pin_number(self, pin_number):
        """Verify pin number.

        :param pin_number: String, pin number
        :return Boolean: True, False
        """
        return True if len(pin_number) == 4 and pin_number.isdigit() else False

    def verify_account_number(self, account_number):
        """Verify mobile number.

        :param account_number: String, account number
        :return Boolean: True, False
        """
        return True if len(account_number) == 16 and account_number.isdigit() else False

    def verify_aadhaar_card_number(self, aadhar_card_number):
        """Verify mobile number.

        :param aadhar_card_number: String, aadhar card number
        :return Boolean: True, False
        """
        account_df = pd.read_csv(self.ACCOUNT_INFO_FILE, dtype=str, header=0)
        for key, value in account_df.iterrows():
            if value['aadhaar_card'] == aadhar_card_number:
                print("\n\n\t\t::::::ERROR::::::\n\t\tAadhaar Card Number already exist in database\n")
                return False
        return True if len(aadhar_card_number) == 16 and aadhar_card_number.isdigit() else False

    def write_data(self, data_frame, filename, column_name):
        """Append the data in filename

        :params data_frame: data frame, row to be written.
        :params filename: file name to write.
        :params columnname: column name of file.
        """
        with open(filename, 'a') as f:
            data_frame.to_csv(f, header=False, index=False, columns=column_name)

    def remove_duplicate(self, filename, column_name):
        account_df = pd.read_csv(filename, dtype=str, header=0)
        clean_account_df = account_df.drop_duplicates(subset='account_id', keep="last")
        clean_account_df.to_csv(filename, header=True, index=False, columns=column_name)



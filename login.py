import os
from base import Base
from verify import Verify

import pandas as pd


class Login(object):
    """Login."""

    def __init__(self):
        """Init."""
        os.system('clear')
        self.base = Base()
        self.verify = Verify()

    def display_beneficiary_account_info(self, account_data):
        """Display the account info. of the beneficiary"""
        print("\t***** BENEFICIARY ACCOUNT DETAILS *****\n")

        filename = self.base.BENEFICIARY_INFO_FILE
        beneficiary_account_df = pd.read_csv(filename, dtype=str, header=0)
        account_data = None
        for key, value in beneficiary_account_df.iterrows():
            if value['u_account_id'] == account_data['account_id']:

                account_data = value
                os.system('clear')
                print("\t***** LOGIN SUCESSFULL *****\n\n")
                break

        print("\tACCOUNT ID :- " + account_data['account_id'])
        print("\tACCOUNT BALANCE :- " + account_data['balance'])
        print("\tFULL NAME :- " + account_data['full_name'])
        print("\tIFSC CODE :- " + account_data['ifsc_code'])
        print("\tMOBILE NUMBER :- " + account_data['mobile_number'])
        print("\tADDRESS :- " + account_data['address'])
        print("\tAADHAAR CARD NUMBER :- " + account_data['aadhaar_card'])

    def get_benificiary(self, account_data):
        """Add beneficiary to the file."""
        print("\t***** ADD BENEFICIARY DETAILS *****\n")
        beneficiary_data = {
            'u_account_id': account_data['account_id'],
            'b_account_id': self.verify.beneficiary_account_id(account_data['account_id']),
            'full_name': self.verify.full_name(),
            'ifsc_code':  self.verify.ifsc_code(),
            'mobile_number': self.verify.mobile_number()
        }
        data_frame = pd.DataFrame(beneficiary_data, index=[0])
        self.base.write_data(data_frame, self.base.BENEFICIARY_INFO_FILE, self.base.BENEFICIARY_COLUMN_NAMES)
        print("\n\t\t***** Beneficiary Successfully added to the file *****\n")

    def display_account_info(self, account_data):
        """Display the account info. of the user"""
        print("\n\n\t\t\t\t\t\t***** ACCOUNT DETAILS *****\n")

        print("\t\t\t\t\t\tACCOUNT ID          :-   " + account_data['account_id'])
        print("\t\t\t\t\t\tACCOUNT BALANCE     :-   " + account_data['balance'])
        print("\t\t\t\t\t\tFULL NAME           :-   " + account_data['full_name'])
        print("\t\t\t\t\t\tIFSC CODE           :-   " + account_data['ifsc_code'])
        print("\t\t\t\t\t\tMOBILE NUMBER       :-   " + account_data['mobile_number'])
        print("\t\t\t\t\t\tADDRESS             :-   " + account_data['address'])
        print("\t\t\t\t\t\tAADHAAR CARD NUMBER :-   " + account_data['aadhaar_card'])

    def display_card_details(self, account_data):
        """Display the card details."""

        print("\t\t\t\t\t\t***** CARD DETAILS *****\n")

        print("\t\t\t\t\t\tCREDIT CARD NUMBER  :- " + account_data['c_number'])
        print("\t\t\t\t\t\tCREDIT CARD PIN     :- " + account_data['c_pin'])
        print("\t\t\t\t\t\tCREDIT CARD CVV     :- " + account_data['c_cvv'])
        print("\n\t\t\t\t\t\tDEBIT CARD NUMBER :- " + account_data['d_number'])
        print("\t\t\t\t\t\tDEBIT CARD PIN      :- " + account_data['d_pin'])
        print("\t\t\t\t\t\tDEBIT CARD CVV      :- " + account_data['d_cvv'] + "\n\n")

    def re_update_account_info(self, account_data):
        print('\n\n\t\t\t\t\t\t***** CHECK YOUR UPDATED INFORMAION *****\n')
        column_name = ['full_name', 'address', 'aadhaar_card', 'mobile_number', 'c_pin', 'd_pin']
        display_name = ['FULL NAME', 'ADDRESS', 'AADHAAR CARD NUMBER', 'MOBILE NUMBER', 'CREDIT CARD PIN',
                        'DEBIT CARD PIN']

        for (d_name, c_name) in zip(display_name, column_name):
            print("\t\t\t\t\t\t"+d_name + " :- " + account_data[c_name])

        user_input = (str(raw_input("\n\t\t\t\t\tEnter Y or y to make changes\n "
                                    "\tor enter anything to Exit : "))).lower()
        if user_input == 'y':
            data_frame = pd.DataFrame(account_data, index=[0])
            self.base.write_data(data_frame, self.base.ACCOUNT_INFO_FILE,
                                 self.base.ACCOUNT_COLUMN_NAMES)
            self.base.remove_duplicate(self.base.ACCOUNT_INFO_FILE,
                                       self.base.ACCOUNT_COLUMN_NAMES)
            print("\t\t\t\t\t***** UPDATED FILE *****\n")
            return account_data
        return account_data

    def update_account_info(self, account_data):
        """Updating the Account information of the user"""
        unchanged_account_data = account_data
        os.system('clear')

        update_page_options = ["UPDATE FULL NAME", "UPDATE ADDRESS",
                              "UPDATE AADHAAR NUMBER", "UPDATE MOBILE NUMBER", "UPDATE CREDIT CARD PIN",
                              "UPDATE DEBIT CARD PIN", "CHECK UPDATED INFORMATION AND EXIT"]

        option_to_func = {'UPDATE FULL NAME': 'self.verify.full_name()',
                          'UPDATE ADDRESS': 'str(raw_input("\tEnter Address: "))',
                          'UPDATE AADHAAR NUMBER': 'self.verify.aadhaar()',
                          'UPDATE MOBILE NUMBER': 'self.verify.mobile_number()',
                          'UPDATE CREDIT CARD PIN': 'self.verify.pin_number()',
                          'UPDATE DEBIT CARD PIN': 'self.verify.pin_number()',
                          'CHECK UPDATED INFORMATION AND EXIT::::': 'None'}

        list_of_df = {'1': 'full_name', '2': 'address', '3': 'aadhaar_number', '4': 'mobile_number', '5': 'c_pin',
                      '6': 'd_pin'}

        while True:
            try:
                print('\n\t\t\t\t\t***** UPDATE YOUR ACCOUNT INFORMATION. *****\n')
                for x, i in enumerate(update_page_options):
                    print('\t\t\t\t\t\tSELECT {} TO {}'.format(x + 1, i))

                print ('\n***NOTE**\n----You have to choose option 7 after choosing option 1 to 6 '
                       'to get your updated info in database.---\n')
                inp = str(raw_input('\nEnter 0 to EXIT. \nEnter your choice : '))
                if inp == '0':
                    return unchanged_account_data
                if inp == '7':
                    return self.re_update_account_info(account_data)
                for row, display in enumerate(update_page_options):
                    if row == (int(inp) - 1) and inp != '7':
                        run_function = option_to_func[update_page_options[row]]
                        column_name = list_of_df[inp]
                        account_data[column_name] = eval(run_function)
                        raw_input('\n\t\t\t\t\tValues Updated.Press Enter to continue. ')
                        break
            except ValueError:
                continue

    def balance_status(self, account_data):
        """Checking the balance of user.
        """
        if account_data['balance'] == 0:
            print"\n\t\t\t\t\t***** ERROR*****\nAccount Balance is {} (low).".format(account_data['balance'])
            self.verify.raise_error()
        else:
            while True:
                try:
                    fund = str(raw_input("\t\t\t\t\tEnter Amount to be transfer :- "))
                    if (int(account_data['balance']) - int(fund)) >= 0 and int(account_data['balance']) != 0:
                        return str(fund)
                    else:
                        print"\n\t\t\t\t\t*****WARNING*****\nAccount Balance is {}.".format(account_data['balance'])
                except ValueError:
                    print("\n\t\t\t\t\t*****WARNING*****\nPlease Enter Amount in number.\n")
                    continue

    def register_credit_cards(self, account_data):
        """Creating new credit card details.
        """
        account_data['c_number'] = self.base.random_generator(16)
        account_data['c_pin'] = self.base.random_generator(4)
        account_data['c_cvv'] = self.base.random_generator(3)
        print("\\n\n\t\t\t\t\t***** NEW CREDIT CARD DETAILS *****\n\n")
        column_name = ['c_number', 'c_pin', 'c_cvv']
        display_name = ['CREDIT CARD NUMBER', 'CREDIT CARD PIN', 'CREDIT CARD CVV']
        self.verify.publish(account_data, display_name, column_name)
        data_frame = pd.DataFrame(account_data, index=[0])
        self.verify.duplicate(data_frame, self.base.ACCOUNT_INFO_FILE, self.base.ACCOUNT_COLUMN_NAMES)

    def register_debit_cards(self, account_data):
        """Registration of new debit card.
        :params account_data: dict, user account data
        """
        account_data['c_number'] = self.base.random_generator(16)
        account_data['c_pin'] = self.base.random_generator(4)
        account_data['c_cvv'] = self.base.random_generator(3)
        print("\t\t\t\t\t***** NEW DEBIT CARD DETAILS *****\n\n")
        column_name = ['d_number', 'd_pin', 'd_cvv']
        display_name = ['DEBIT CARD NUMBER', 'DEBIT CARD PIN', 'DEBIT CARD CVV']
        self.verify.publish(account_data, display_name, column_name)
        data_frame = pd.DataFrame(account_data, index=[0])
        self.verify.duplicate(data_frame, self.base.ACCOUNT_INFO_FILE, self.base.ACCOUNT_COLUMN_NAMES)

    def authenticate(self):
        """Authenticate the user."""
        os.system('clear')
        print"\t\t\t\t\t\t\t\t***** WELCOME TO NOBANK *****"
        retry = 0
        while retry < 5:
            flag = 0
            account_id = str(raw_input("\n\t\t\t\t\t\tEnter 16 Digit Account Id : "))
            full_name = str(raw_input("\t\t\t\t\t\tEnter Full Name : "))
            filename = self.base.ACCOUNT_INFO_FILE
            account_df = pd.read_csv(filename, dtype=str, header=0)
            account_data = None
            for key, value in account_df.iterrows():
                if value['account_id'] == account_id and value['full_name'] == full_name:
                    flag = 1
                    account_data = value
                    os.system('clear')
                    print "\n\n\t\t\t\tWELCOME {}.".format(full_name).upper()
                    print("\t\t\t\t\t\t\t\t***** LOGIN SUCESSFULL ****\n\n")
                    break

            if flag == 0:
                retry += 1
                os.system('clear')
                print("\t\t\t\t\t\t\t\t***** LOGIN FAILED *****\n")
                print"\t\t\t\t\t\t Enter correct details (remaining retry:- {})\n".format(5 - retry)

            else:
                return account_data.to_dict()

    def transfer_fund(self, account_data):
        """Transfer fund."""
        try:
            transfer_amount = self.balance_status(account_data)
            payer_account_id = self.verify.beneficiary_account_id()
            if payer_account_id == account_data['account_id']:
                self.verify.raise_error()
            found_account_data = None
            filename = self.base.ACCOUNT_INFO_FILE
            account_df = pd.read_csv(filename, dtype=str, header=0)
            for key, value in account_df.iterrows():
                if value['account_id'] == payer_account_id:
                    found_account_data = value.to_dict()
            remaining_balance = str(int(account_data['balance']) - int(transfer_amount))
            account_data['balance'] = remaining_balance
            ifsc_code = self.verify.ifsc_code()
            list_row = [account_data]
            if found_account_data:
                found_account_data['balance'] = str(int(found_account_data['balance']) + int(transfer_amount))
                list_row.append(found_account_data)
            data_frame = pd.DataFrame(list_row)
            self.verify.duplicate(data_frame, self.base.ACCOUNT_INFO_FILE,
                                                   self.base.ACCOUNT_COLUMN_NAMES)
            os.system('clear')
            print "\n\t\t\t\t\t***** TRANSACTION SUCESSFULL *****"
            print "\n\t\t\t\t\tYour account balance is {}".format(remaining_balance)
            print "\n\n\t\t\t\t\tSent to Account Id :- {}".format(payer_account_id)
            print "\n\t\t\t\t\tAmount :- {}".format(transfer_amount)
            print "\n\t\t\t\t\tIFSC Code :- {}\n\n".format(ifsc_code)

        except ValueError:
            print "\n\t\t\t\t\t***** TRANSACTION FAILED *****\n"

    def login_page(self, account_data):
        login_page_options = ["DISPLAY ACCOUNT INFORMATION", "DISPLAY LIST OF BENEFICIARIES",
                              "DISPLAY LIST OF CARDS DETAILS", "ADD BENEFICIARIES", "TRANSFER FUNDS",
                              "UPDATE ACCOUNT INFORMATION", "REGISTER NEW CREDIT CARD", "REGISTER NEW DEBIT CARD",
                              "EXIT"]

        option_to_func = {'DISPLAY ACCOUNT INFORMATION': self.display_account_info,
                          'DISPLAY LIST OF BENEFICIARIES': self.display_beneficiary_account_info,
                          'DISPLAY LIST OF CARDS DETAILS': self.display_card_details,
                          'ADD BENEFICIARIES': self.get_benificiary,
                          'TRANSFER FUNDS': self.transfer_fund,
                          'UPDATE ACCOUNT INFORMATION': self.update_account_info,
                          'REGISTER NEW CREDIT CARD': self.register_credit_cards,
                          'REGISTER NEW DEBIT CARD': self.register_debit_cards,
                          'EXIT': None}
        while True:
            for x, i in enumerate(login_page_options):
                print('\t\t\t\tSELECT {} TO {}'.format(x + 1, i))
            opt = str(raw_input('\n\n\t\t\t\t\t\tENTER OPTION TO PROCEED: '))

            try:
                os.system('clear')
                value = option_to_func[login_page_options[int(opt) - 1]](account_data)
                raw_input('\nPRESS ENTER TO CONTINUE...')
                if value:
                    account_data = value
                os.system('clear')

            except ValueError:
                break

    def login_main_page(self):
        """Main login page."""
        os.system('clear')
        while True:
            print"\n\t\t\t\t\t\t\t\t***** WELCOME TO NOBANK *****\n\n"
            print "\t\t\t\t1. LOGIN PAGE \t\t\t\t\t\t\t\t2. EXIT"
            ch = str(raw_input("\n\tPRESS 1 to Proceed :- "))
            try:
                if ch == '1':
                    account_data = self.authenticate()
                    if account_data:
                        self.login_page(account_data)
                elif ch == '2':
                    print("\n\tThank You !! Visit Again\n")
                    break
                else:
                    print("Wrong Option")
            except Exception:
                str(raw_input("\t\t\t\t\tENTER TO CONTINUE... : "))
                os.system('clear')
                continue


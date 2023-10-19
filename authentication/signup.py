import json
from shared.hash import *


class SignUp:
    roles = {'1': "doctor", '2': "other_staff"}

    def create_new_user(self):

        name = input('Username:')
        password = input('Enter a password including an upper-case letter, lower-case letter, a digit and length not less than 5: \n')
        while True:
            if not (any(x.isupper() for x in password) and
                    any(x.islower() for x in password) and 
                    any(x.isdigit() for x in password) and 
                    len(password) >= 5):
                password = input("Password is too weak. Please re-enter a new password: ")
            else:
                break
        safe_password = hash_password(password)

        # read config file for doctor and other_staff codes
        with open("data/data/config.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            doc_code = data['codes'].get('doctor')
            rec_code = data['codes'].get('other_staff')

        # hotel staff accounts can only be created by using the relevant code for security
        while True:

            role_number = input('Press 1 for "doctor account" or 2 for "other_staff account": ')

            if role_number == '1':
                code = hash_password(input("Please enter the doctor code to create account: "))
                if code == doc_code:
                    user_type = self.roles.get('1')
                    privilege_level = '2'
                    break
                else:
                    print("Invalid code")

            elif role_number == '2':
                code = hash_password(input("Please enter the other_staff code to create account: "))
                if code == rec_code:
                    user_type = self.roles.get('2')
                    privilege_level = '3'
                    break
                else:
                    print("Invalid code")
            else:
                print("Invalid input. Try again")

        # read and write user to config file
        with open("data/config.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            user_id = len(data['users'])+1
            data['users'].append({
                'id': user_id,
                'name': name,
                'password': safe_password,
                'user_type': user_type,
                'privilege_level': privilege_level
            })
        with open("data/config.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Account created successfully")

        # fill account details
        print("Fill in personal account details")
        acc_name = input('Your name: ')
        age = input('Age: ')
        nic = input('NIC number: ')
        tel = input('Telephone number: ')

        # write account details to data file
        with open("data/data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['personal_details'].append({
                'id': user_id,
                'name': acc_name,
                'age': age,
                'nic': encode(nic),
                'tel': encode(tel)
            })
        with open("data/data.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Account completed")



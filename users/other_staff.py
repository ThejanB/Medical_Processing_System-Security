import json
from shared.hash import *
from shared.edit_account import *

class Other_staff:

    def run(self,current_user_id):
        print("Press 1 to create patient account\nPress 2 to edit personal account\nPress 3 to view personal account\nPress 4 to set new password\nPress -1 to exit\n ")
        while True:
            option = input()
            if option == '1':
                Other_staff().create_patient_account()
                print("Press next number: ")
            elif option == '2':
                edit_account(current_user_id)
                print("Press next number: ")
            elif option == '3':
                view_account(current_user_id)
                print("Press next number: ")
            elif option == '4':
                renew_password(current_user_id)
                print("Press next number: ")
            elif option == '-1':
                print("Thank you other_staff")
                break
            else:
                print("Invalid input. Try again")

    @staticmethod
    def create_patient_account():
        try:
            name = input('Patient username: ')
            temp_password = hash_password(input('Password: '))

            # read and write user to config file
            with open("data/config.json", 'r') as json_data_file:
                data = json.load(json_data_file)
                patient_id = len(data['users'])+1
                data['users'].append({
                    'id': patient_id,
                    'name': name,
                    'password': temp_password,
                    'user_type': "patient",
                    'privilege_level': '4'
                })
            with open("data/config.json", 'w') as outfile:
                json.dump(data, outfile)

            print("Please enter personal details of new patient")

            patient_name = input('Patient name: ')
            nic = input('NIC number: ')
            age = input('Age: ')
            tel = input('Telephone number: ')

            # read and write patient details to data file
            with open("data/data.json", 'r') as json_data_file:
                data = json.load(json_data_file)
                data['personal_details'].append({
                    'id': patient_id,
                    'name': patient_name,
                    'age': age,
                    'nic': encode(nic),
                    'tel': encode(tel)
                })
            with open("data/data.json", 'w') as outfile:
                json.dump(data, outfile)

            print("Other staff account created successfully")

        except FileNotFoundError:
            print("File not found. Please ensure the file exists.")







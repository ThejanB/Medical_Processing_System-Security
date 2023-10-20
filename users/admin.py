from shared.hash import *
import json

class Admin:
    def run(self):
       
        while True:
            role_number = input("Press 1 to edit doctor code\nPress 2 to edit other_staff code\nPress 3 to create admin account\nPress -1 to logout\n")

            if role_number == '1':
                self.change_doctor_code()

            elif role_number == '2':
                self.change_other_staff_code()

            elif role_number == '3':
                self.create_admin()

            elif role_number == '-1':
                print("Admin logout!\n")
                break
            else:
                print("Invalid input")

    @staticmethod
    def create_admin():
        name = input('Admin username: ')
        temp_password = hash_password(input('Temporary password: '))

        try:
            # Read the data from the file
            with open("data/config.json", 'r') as json_data_file:
                data = json.load(json_data_file)

            # Update the data in memory
            admin_id = len(data['users']) + 1
            data['users'].append({
                'id': admin_id,
                'name': name,
                'password': temp_password,
                'user_type': "admin",
                'privilege_level': '1'
            })

            # Write the updated data back to the file
            with open("data/config.json", 'w') as json_data_file:
                json.dump(data, json_data_file)

            print("Please enter personal details of admin")

            admin_name = input('Admin name: ')
            age = input('Age: ')
            nic = input('NIC number: ')
            tel = input('Telephone number: ')

            # read and write admin details to data file
            with open("data/data.json", 'r') as json_data_file:
                data = json.load(json_data_file)
                data['personal_details'].append({
                    'id': admin_id,
                    'name': admin_name,
                    'age': age,
                    'nic': encode(nic),
                    'tel': encode(tel)
                })
            with open("data/data.json", 'w') as outfile:
                json.dump(data, outfile)

            print("New admin account created successfully\n")

        except FileNotFoundError:
            print("File not found. Please ensure the file exists.")

    @staticmethod
    def change_doctor_code():
        doc_code = hash_password(input("Enter new doctor code: "))

        with open("data/config.json", 'r') as json_data_file:
            data = json.load(json_data_file)

            # change doctor code
            data['codes'] = {
                'doctor': doc_code,
                'other_staff': data['codes'].get('other_staff'),
            }

        with open("data/config.json", 'w') as outfile:
            json.dump(data, outfile)
                    
        print("New doctor code set successfully\n")

    @staticmethod
    def change_other_staff_code():
        other_staff_code = hash_password(input("Enter new other_staff code: "))

        try:
            with open("data/config.json", 'r') as json_data_file:
                data = json.load(json_data_file)

            # Change the 'other_staff' code
            data['codes']['other_staff'] = other_staff_code

            with open("data/config.json", 'w') as outfile:
                json.dump(data, outfile)
            
            print("New other_staff code set successfully\n")

        except FileNotFoundError:
            print("Config file not found. Please ensure the file exists.\n")





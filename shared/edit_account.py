import json
from shared.hash import *


def edit_account(user_id):
    new_name = input('Enter new name: ')
    new_age = input('Enter new age: ')
    new_tel = input('Enter new telephone no: ')

    # read and write new account details to data file
    with open("data/data.json", 'r') as data_file:
        f_data = json.load(data_file)
        details = f_data['personal_details']
        for i in range(len(details)):
            if user_id == str(details[i]['id']):

                details[i]['name'] = new_name
                details[i]['age'] = new_age
                details[i]['tel'] = encode(new_tel)

    with open("data/data.json", 'w') as f_outfile:
        json.dump(f_data, f_outfile)

    print("Account updated successfully")


def view_account(user_id):
    # read account details from data file
    with open("data/data.json", 'r') as data_file:
        f_data = json.load(data_file)
        details = f_data['personal_details']
        for i in range(len(details)):
            if user_id == str(details[i]['id']):
                print("Account name: " + details[i]['name'])
                print("Age: " + details[i]['age'])
                print("NIC number: " + decode(details[i]['nic']))
                print("Telephone: " + decode(details[i]['tel']))


def renew_password(user_id):
    new_pwd = input('Enter a password including an upper-case letter, lower-case letter, a digit and length not less than 6: \n')
    while True:
        if not (any(x.isupper() for x in new_pwd) and any(x.islower() for x in new_pwd) and any(x.isdigit() for x in new_pwd) and len(new_pwd) >= 6):
            new_pwd = input("Password is too weak. Please re-enter: ")
        else:
            break
    new_password = hash_password(new_pwd)

    with open("data/config.json", 'r') as data_file:
        f_data = json.load(data_file)
        account = f_data['users']
        for i in range(len(account)):
            if user_id == str(account[i]['id']):
                account[i]['password'] = new_password

    with open("data/config.json", 'w') as f_outfile:
        json.dump(f_data, f_outfile)
    print("Password updated successfully")






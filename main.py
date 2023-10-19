from authentication.signup import SignUp
from authentication.login import Login
from users.admin import Admin
from users.other_staff import Other_staff
from users.doctor import Doctor
from users.patient import Patient
from shared.edit_account import *
from shared.check_patient_id import check_patient_id


def runApp():

    current_user = Login().auth_user()
    if current_user:
        current_user_id = str(current_user.get('id'))

        # user is admin
        if current_user.get('privilege_level') == '1':
            Admin().run()

        # user is a other_staff
        elif current_user.get('privilege_level') == '3':
            Other_staff().run(current_user_id)
            
        # user is a doctor
        if current_user.get('privilege_level') == '2':
            print("Press 1 to add sickness details \nPress 2 to add drug prescription \nPress 3 to view sickness details \nPress 4 to view previous drug prescriptions \nPress 5 to edit account \nPress 6 to renew password \nPress 7 to view account\nPress -1 to exit\n ")

            while True:
                option = input()
                if option in ['1', '2', '3', '4']:

                    while True:
                        patient_id = input("Enter patient id: ")
                        if check_patient_id(patient_id):
                            break
                        else:
                            print("Invalid patient id")

                    if option == '1':
                        Doctor().add_sickness_details(patient_id)
                        print("Press next number: ")
                    elif option == '2':
                        Doctor().add_drug_prescription(patient_id)
                        print("Press next number: ")
                    elif option == '3':
                        Doctor().read_sickness_details(patient_id)
                        print("Press next number: ")
                    elif option == '4':
                        Doctor().read_drug_prescription(patient_id)
                        print("Press next number: ")
                elif option == '5':
                    edit_account(current_user_id)
                    print("Press next number: ")
                elif option == '6':
                    renew_password(current_user_id)
                    print("Press next number: ")
                elif option == '7':
                    view_account(current_user_id)
                    print("Press next number: ")
                elif option == '-1':
                    print("Doctor logout!")
                    break
                else:
                    print("Invalid input. Try again")

        # user is a patient
        if current_user.get('privilege_level') == '4':
            print("Press 1 to change password \nPress 2 to update account \nPress 3 to view account details\nPress 4 to view sickness details \nPress 5 to view previous drug prescriptions \nPress 6 to view lab test prescription \nPress -1 to exit\n ")
            while True:
                option = input()
                if option == '1':
                    renew_password(current_user_id)
                    print("Press next number: ")
                elif option == '2':
                    edit_account(current_user_id)
                    print("Press next number: ")
                elif option == '3':
                    view_account(current_user_id)
                    print("Press next number: ")
                elif option == '4':
                    Patient().read_sickness_details(current_user_id)
                    print("Press next number: ")
                elif option == '5':
                    Patient().read_drug_prescription(current_user_id)
                    print("Press next number: ")
                elif option == '-1':
                    print("Thank you")
                    break
                else:
                    print("Invalid input. Try again")

if __name__ == '__main__':

    while True:

        print("Press 1 to login\nPress 2 to signup\nPress -1 to exit\n")
        n = input("choice: ")
        if n == '1':
            runApp()
        elif n == '2':
            SignUp().create_new_user()
            print("Login to your account")
            runApp()
        elif n == '-1':
            break
        else:
            print("Invalid input. Try again")



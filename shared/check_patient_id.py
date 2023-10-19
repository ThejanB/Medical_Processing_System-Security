import json


def check_patient_id(patient_id):
    with open("data/config.json", 'r') as data_file:
        f_data = json.load(data_file)
        users = f_data['users']
        for user in users:
            if patient_id == str(user['id']) and user['user_type'] == 'patient':
                return True
        else:
            return False


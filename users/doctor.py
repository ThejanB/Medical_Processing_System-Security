import json
from datetime import datetime
class Doctor:

    @staticmethod
    def add_sickness_details(patient_id):

        sickness_details = input("Enter sickness details: \n")

        try:
            with open("data/data.json", 'r') as json_data_file:
                data = json.load(json_data_file)

            # Append sickness details
            data['sickness_details'].append({
                'id': patient_id,
                'sickness': sickness_details,
                'date': str(datetime.now())[:19],
            })

            with open("data/data.json", 'w') as outfile:
                json.dump(data, outfile)

            print("Sickness details added")

        except FileNotFoundError:
            print("Data file not found. Please ensure the file exists.")
        except json.JSONDecodeError:
            print("Error decoding JSON data in the file.")

    @staticmethod
    def add_drug_prescription(patient_id):

        while drug_prescription == '':
            drug_prescription = input("Enter drug prescription: \n")
            if drug_prescription == '':
                print("Drug prescription cannot be empty")

        # write drug prescription to data file
        with open("data/data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['drug_presc'].append({
                'id': patient_id,
                'drug_presc': drug_prescription,
                'date': str(datetime.now())[0:19],
            })
        with open("data/data.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Drug prescription details added")

    @staticmethod
    def read_sickness_details(patient_id):

        # read sickness details from data file
        with open("data/data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['sickness_details']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['sickness'])

    @staticmethod
    def read_drug_prescription(patient_id):

        # read drug prescription from data file
        with open("data/data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['drug_presc']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['drug_presc'])

import json
from shared.hash import hash_password

class Login:

    @staticmethod
    def auth_user():
        result = 'Login failed'
        
        name = input("Enter username: ")
        hashed_password = hash_password(input("Enter password: "))

        with open("data/config.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            for user in data['users']:
                if name == user['name'] and hashed_password == user['password']:
                    current_user = user
                    result = "Login successful"
        print(result)
        if result == "Login successful":
            return current_user
        else:
            return False



import requests
import os
import dotenv


dotenv.load_dotenv()

class Users:

    def __init__(self):
        sheet_token = os.getenv("sheet_token")
        self.header = {
             "Authorization": f"Bearer { sheet_token }",
        }


    def user_input(self):
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        email = input("What is your email?\n")
        check_email = input("Type your email agin\n")

        while True:
            if email != check_email:
                print("Unsuccessful. Your e-mail does not match.")
            else:
                new_data = {
                    "user": {
                        "firstName": first_name,
                        "lastName": last_name,
                        "email": email,
                    },
                }

                response = requests.post(url="https://api.sheety.co/aaa6d653bc8798ed5961737447248fad/flightDeals/users", json=new_data, headers=self.header)
                print(response.text)
                break

                # print("Success! Your email has been added")

users = Users()
users.user_input()
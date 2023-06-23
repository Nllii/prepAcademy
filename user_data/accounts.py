from http import client
import os 
import sys
import json
import re


master_record = os.listdir("masterdb")

class academyAccount:
    """This class is responsible for creating and managing user accounts"""
    @staticmethod
    def findAccount(record_find):
        """each user gets a folder with their account number as the folder name
        Requires:
            - account_number
            
        """
        print(record_find)
        if record_find['date_of_birth']:
            # make sure its a valid date
            if len(record_find['date_of_birth']) != 10:
                return "Invalid date of birth use MM-DD-YYYY format (ex. 03-22-2001)"
        valid_email = re.search(r"[^@]+@[^@]+\.[^@]+", record_find['email'])
        if not valid_email:
            return "Invalid email address"
            
        regex_record = record_find['date_of_birth'].replace("-","_")
        regex_email = record_find['email'].replace("@","_")
        for account in master_record:
            if account == regex_record:
                print(account)
                with open(f"masterdb/{account}/account{regex_email}.json", "r") as account_file:
                    account_data = json.load(account_file)
                    for email_address in account_data:
                        try:
                            if account_data[email_address]["email"] == record_find['email']:
                                return account_data[email_address]
                        except Exception as e:
                            return "requested parameter not found"
        #create a new account
        # make directory based on date of birth and add account.json
        print(f"Account not found in masterdb for {regex_record}")       
        
        if not os.path.exists(f"masterdb/{account}/account{regex_email}.json"):
            try:
                os.mkdir(f"masterdb/{regex_record}")
            except Exception as e:
                print(e)
            with open(f"masterdb/{regex_record}/account{regex_email}.json", "w") as account_file:
                json.dump(record_find, account_file, indent=4)
            return record_find
        
        
    @staticmethod
    def Useraccount(client_request):
        """Create a new account if the user does not have one
        """
        # print("requested_info",client_request)
        try:
                
            if client_request["date_of_birth"] == "":
                return "Date of birth is required"
            
            if client_request["email"] == "":
                return "Email address is required"
        except Exception as e:
            print(e)
            return "Missing required parameters (this is a curtousy message)"
        # client_dict = {
        #     "account_number": "",
        #     "created_at": "",
        #     "last_login": "",
        #     "username": "",
        #     "password": "",
        #     "email": client_request["email_address"],
        #     "date_of_birth": client_request["date_of_birth"],
        #     "first_name": "",
        #     "last_name": "",
        #     "address": "",
        #     "city": "",
        #     "state": "",
        #     "zip_code": "",
        #     "country": "",
        #     "phone_number": "",
        #     "account_type": "",
        #     "account_status": "",
        #     "account_balance": "",
        #     "amount": "",


        # }
        
        client_account = academyAccount.findAccount(client_request)
        return client_account




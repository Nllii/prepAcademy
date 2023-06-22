import os 
import sys
import json


master_record = os.listdir("masterdb")

class academyAccount:
    """This class is responsible for creating and managing user accounts"""
    
    @staticmethod
    def findAccount(account_number):
        """each user gets a folder with their account number as the folder name
        Requires:
            - account_number
        """
        for account in master_record:
            if account == account_number:
                return True
        print("Account not found")
        return False
        
        
    
    @staticmethod
    def Useraccount(account_number):
        """Create a new account if the user does not have one
        """
        print("account_number",account_number)
        return_dict = {
            "account_number": "",
            "created_at": "",
            "last_login": "",
            "username": "",
            "password": "",
            "email": "",
            "first_name": "",
            "last_name": "",
            "address": "",
            "city": "",
            "state": "",
            "zip_code": "",
            "country": "",
            "phone_number": "",
            "account_type": "",
            "account_status": "",
            "account_balance": "",
            "account_currency": "",

        }

        found_account = academyAccount.findAccount(account_number)
        
        if (found_account) != True:
            print("Creating new account")
            
        
        return return_dict




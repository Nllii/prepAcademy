"""test all functions calls in the projects"""
# from user_data import accounts
import requests
import json

patron = {
    
    "email_address": "a@a.com",
    "date_of_birth": "03-22-2001",
    "date_contribution": "1 Nov, 10:20 AM",
    "id": "#1236",
    "email": "michael.lawson@reqres.in",
    "first_name": "Michael",
    "last_name": "Lawson",
    "avatar": "https://reqres.in/img/faces/7-image.jpg",
    "account_queue": "1",
    "amount": "50,00",
    "status": "Paid",
    "account_number": "",
    "created_at": "",
    "last_login": "",
    "username": "",
    "password": "",
    "date_of_birth": "",
    "address": "",
    "city": "",
    "state": "",
    "zip_code": "",
    "country": "",
    "phone_number": "",
    "account_type": "",
    "account_status": "",
    "account_balance": ""
    
}

convert_data = json.dumps(patron)

local_request = requests.get("http://127.0.0.1:5000/account/transactions", json=convert_data)
# resp = local_request.json()
print(local_request)


# user_database = accounts.academyAccount()
# user_database.Useraccount(f"{patron}")


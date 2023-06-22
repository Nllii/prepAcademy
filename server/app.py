# save this as app.py
import os
import sys
# This isn't necessary if you do `pip install -e .` but for local development its done this way(remove during deployment)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask import request
from flask import jsonify
from user_data import accounts





app = Flask(__name__)
user_database = accounts.academyAccount()

@app.route("/status")
def status():
    return "server is running"



# @app.route('/account/<user_id>', methods = ['GET', 'POST', 'DELETE'])
@app.route('/account', methods = ['GET', 'POST', 'DELETE'])
def userAccount():
    # Customer Name
    # username
    # Email
    # Account Number (if available)
    # returns a 201 code to indicate that the account was created successfully
    
    if request.method == 'POST':
        data = request.get_json()
        account_info = user_database.Useraccount(data)
        response = {
            "response": account_info
        }
        return jsonify(response), 201


    



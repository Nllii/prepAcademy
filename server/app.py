# save this as app.py
import os
import sys
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



@app.route('/account/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def userAccount(user_id):
    # Customer Name
    # username
    # Email
    # Account Number (if available)
    if request.method == 'POST':
        data = request.get_json()
        user_database.Useraccount(data)
        return jsonify(data), 201


    



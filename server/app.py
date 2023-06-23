# save this as app.py
import os
import sys
# This isn't necessary if you do `pip install -e .` but for local development its done this way(remove during deployment)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask import request
from flask import jsonify
from user_data import accounts
user_database = accounts.academyAccount()
app = Flask(__name__)
@app.route("/status")
def status():
    return "server is running"



# @app.route('/account/<user_id>', methods = ['GET', 'POST', 'DELETE'])
@app.route('/account', methods = ['GET', 'POST', 'DELETE'])
def userAccount():
    """
    This function is responsible for creating and managing user accounts

    Returns:
        str: json response, 201 if successful, 400 if not
    """
    
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        account_info = user_database.Useraccount(data)
        response = {
            "response": account_info
        }
        return jsonify(response), 201


    

@app.route('/account/transactions', methods = ['GET', 'POST', 'DELETE'])
def generated_revenue():
    # populate the frontend with reqired data.
    if request.method == 'GET':
        data = request.get_json()
        print(data)
        account_info = user_database.Useraccount(data)
        response = {
            "response": account_info
        }
        return jsonify(account_info), 201
    return "<h3>...server is running</h3>"

    


if __name__ == "__main__":
    app.run(debug=True)

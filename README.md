# prepAcademy 

# [project suspended] DO NOT USE:

### REASON: 
1. Client does not have a legitimate business standing to sign up for required APIs for intergations
2. Client hintted on a scrupulous bussiness practice (vapourware concept )
3. Client can't provide a basic prosopal
4. Client is not coherent enough to understand basic concepts
5. Client does not have the funding required for such an implementation of concept
6. Client is not willing to pay for the services required to implement the concept
7. Client is not willing to sign a contract for the services required to implement the concept


## [showcase demo frontend]
![screenshot](https://github.com/Nllii/prepAcademy/blob/6ff5a9647dc5368849ae6c758cc3a4ca2b80a2fb/masterdb/demo-1.jpeg)

proof of concept apis(endpoints) and backend for prepAcademy
REST on flask 

# DOCUMENTATION (Alpha version 0.0.1)

```payment_data api request to the server```
- ```payment_id (generated by the server and mapped to the user)```
- ```payment_amount```
- ```payment_date```
- ```payment_status```
- ```payment_type```
- ```payment_currency```

1. ```findAccount``` checks if the user exists in the database. In the future, this will be replaced by an actual database; not file storage.
response dictionary:
```bash
"account_number": "",
"created_at": "",
"last_login": "",
"username": "",
"password": "",
"email": "",
"date_of_birth": "",
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
```







#### TODO Backend: 
- implement a user registration system  ```call findAccount()``` (complete).
- implement a user authentication system.
- implement a user login system.
    - implement a user login history system to prevent session hijacking.
- implement a user logout system.
- implement a user profile system.
- implement a user payment system.
- implement a user payment history system.
- implement a user payment status system.
- implement a user payment type system.
- either implement a 3rd party payment gateway or implement a dummy payment gateway.
- move database to a cloud service like mongoDB for scalability.


#### TODO Frontend: 
- javascript(react.js) frontend.


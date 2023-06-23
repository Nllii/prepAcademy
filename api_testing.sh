#!bin/bash


# use curl to test api endpoints locally
server_endpoint=http://127.0.0.1:5000
# echo $status_code # 200 if server is running

server_status(){
    curl $server_endpoint/status 


}
find_account(){
    # creates and returns a new account 
    curl -X POST -H "Content-Type: application/json" -d '{"email_addres":"a@a.com","date_of_birth":"03-22-2001"}' $server_endpoint/account
}





# test_account={
#     "email_addres": "a@a.com",
#     "date_of_birth": "03-22-2001",
#     "date_contribution": "1 Nov, 10:20 AM",
#     "id": "#1236",
#     "email": "michael.lawson@reqres.in",
#     "first_name": "Michael",
#     "last_name": "Lawson",
#     "avatar": "https://reqres.in/img/faces/7-image.jpg",
#     "account_queue": "1",
#     "price": "50,00",
#     "status": "Paid",
#     "account_number": "",
#     "created_at": "",
#     "last_login": "",
#     "username": "",
#     "password": "",
#     "address": "",
#     "city": "",
#     "state": "",
#     "zip_code": "",
#     "country": "",
#     "phone_number": "",
#     "account_type": "",
#     "account_status": "",
#     "account_balance": ""



contribute()
{
    
    curl -X POST -H "Content-Type: application/json" -d '{"email_addres":"a@a.com","date_of_birth":"03-22-2001"}' $server_endpoint/account

}
remove_account(){
    # removes an account
    curl -X DELETE -H "Content-Type: application/json" -d '{"email_addres":""}' $server_endpoint/account
}









"${@:1}" "${@:3}"

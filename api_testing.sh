#!bin/bash


# use curl to test api endpoints locally
server_endpoint=http://127.0.0.1:5000
# echo $status_code # 200 if server is running

server_status(){
    curl $server_endpoint/status 


}
find_account(){
    
    curl -X POST -H "Content-Type: application/json" -d '{"username":"testa","email":"test"}' $server_endpoint/account/1234


}

"${@:1}" "${@:3}"

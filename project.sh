#!bin/bash


push(){
    git add .
    read -p "Enter commit message: " message
    git commit -am  "$message"
    git push 
}

# run flask server
flask_run(){
    export FLASK_APP=/Users/codeserver/prepAcademy/server/app.py
    # export FLASK_ENV=development
    flask run 
}

kill_server(){
    # lsof -P | grep ":$process_to_kill" | awk '{print $2}' | xargs kill -9

    kill -9 $(lsof -t -i:5000)
}

"${@:1}" "${@:3}"


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

"${@:1}" "${@:3}"


#!bin/bash


push(){
    git add .
    read -p "Enter commit message: " message
    git commit -am "message"
    git push 
}

"${@:1}" "${@:3}"


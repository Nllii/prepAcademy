#!bin/bash


push(){
    git add .
    git commit -am "update"
    git push 
}

"${@:1}" "${@:3}"


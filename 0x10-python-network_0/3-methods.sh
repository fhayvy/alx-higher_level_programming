#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -i -L -X OPTIONS "$1"
#curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

#!/bin/bash
# request to a URL passed as an argument
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)

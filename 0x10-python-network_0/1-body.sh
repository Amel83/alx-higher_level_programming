#!/bin/bash

# Check if a URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a GET request to the URL, follow redirects, and store the response in a variable
response=$(curl -sL "$url")

# Get the HTTP status code from the response
http_status=$(echo "$response" | head -n 1 | awk '{print $2}')

# Check if the status code is 200 (OK)
if [ "$http_status" -eq 200 ]; then
    # Extract and display the body of the response
    echo "$response" | sed '1,/^$/d'
else
    echo "HTTP Status Code: $http_status"
fi

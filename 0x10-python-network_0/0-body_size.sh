#!/bin/bash

# Check if a URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a HEAD request to the URL and store the result in a variable
response=$(curl -sI "$url")

# Extract the Content-Length header from the response and display it (in bytes)
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')
if [ -n "$content_length" ]; then
    echo "$content_length"
else
    echo "Content-Length header not found in the response."
fi

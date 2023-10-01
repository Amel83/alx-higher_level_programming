#!/bin/bash

# Check if a URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a request to the URL and store the HTTP status code in a variable
http_status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Display the HTTP status code
echo "$http_status_code"

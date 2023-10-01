#!/bin/bash

# Check if a URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a GET request to the URL with the X-School-User-Id header and store the response in a variable
response=$(curl -s -H "X-School-User-Id: 98" "$url")

# Display the body of the response
echo "$response"

#!/bin/bash

# Check if a URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send an OPTIONS request to the URL and store the response in a variable
response=$(curl -sI -X OPTIONS "$url")

# Extract and display the Allow header from the response (contains the accepted methods)
allowed_methods=$(echo "$response" | grep -i "Allow" | awk '{print $2}')

# Display the list of allowed HTTP methods
echo "$allowed_methods"


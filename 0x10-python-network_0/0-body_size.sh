#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
url="$1"
response=$(curl -sI "$url")
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')
if [ -n "$content_length" ]; then
    echo "$content_length"
else
    echo "Content-Length header not found in the response."
fi

#!/usr/bin/python3
import sys

# Initialize variables to hold the metrics
total_file_size = 0
status_code_counts = {}

try:
    # Read stdin line by line
    for line_number, line in enumerate(sys.stdin, 1):
        # Extract the relevant information from the input line
        line = line.strip()
        parts = line.split(" ")
        file_size = int(parts[-1])
        status_code = parts[-2]

        # Update the total file size
        total_file_size += file_size

        # Update the status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

        # Check if 10 lines have been processed
        if line_number % 10 == 0:
            # Print the metrics
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")

# Handle keyboard interruption (CTRL + C)
except KeyboardInterrupt:
    # Print the final metrics
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")


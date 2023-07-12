#!/usr/bin/python3
""" import"""
import sys


total_file_size = 0
status_code_counts = {}

try:
    
    for line_number, line in enumerate(sys.stdin, 1):
    
        line = line.strip()
        parts = line.split(" ")
        file_size = int(parts[-1])
        status_code = parts[-2]

    
        total_file_size += file_size

    
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

    
        if line_number % 10 == 0:
  
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")


except KeyboardInterrupt:
    
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")


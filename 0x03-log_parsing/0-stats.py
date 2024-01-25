#!/usr/bin/python3
"""scripts that reads stdin line by line"""

import sys
import re

def process_line(line):
    """
    Process a line and extract relevant information.

    :param line: The input line.
    :return: A tuple containing IP address, status code, and file size.
    """
    # Define the regex pattern for extracting information from the line
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    
    match = re.match(pattern, line)
    if match:
        ip_address, status_code, file_size = match.groups()
        return ip_address, int(status_code), int(file_size)
    else:
        return None, None, None

def print_statistics(total_size, status_counts):
    """
    Print statistics including total file size and number of lines by status code.

    :param total_size: Total file size.
    :param status_counts: Dictionary containing counts for each status code.
    """
    print(f"Total file size: {total_size}")
    print("Number of lines by status code:")
    for status_code in sorted(status_counts):
        count = status_counts[status_code]
        print(f"{status_code}: {count}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            ip_address, status_code, file_size = process_line(line)
            if ip_address is not None:
                total_size += file_size
                status_counts[status_code] += 1

            # Print statistics every 10 lines
            if line_number % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
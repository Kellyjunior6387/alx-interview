#!/usr/bin/python3
import sys
import signal

# Initialize counters and variables
total_file_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                      405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Prints the computed statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL+C) to print statistics."""
    print_statistics()
    sys.exit(0)


# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)
# Process each line from standard input
for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts) < 7:
        continue
    ip_address = parts[0]
    date = parts[3] + " " + parts[4]
    method = parts[5]
    path = parts[6]
    protocol = parts[7]
    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
    except ValueError:
        continue
    # Validate the request format
    if method != '"GET' or path != '/projects/260' or protocol != 'HTTP/1.1"':
        continue
    # Update metrics
    total_file_size += file_size
    if status_code in status_codes_count:
        status_codes_count[status_code] += 1
    line_count += 1
    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_statistics()
print_statistics()

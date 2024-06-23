import sys
import signal

# Initialize variables
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Print the statistics of the logs."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print("{}: {}".format(code, status_code_count[code]))

def signal_handler(sig, frame):
    """Handle the keyboard interruption signal."""
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Check if the line matches the specified format
        parts = line.split()
        if len(parts) < 9:
            continue

        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        method = parts[5][1:]
        endpoint = parts[6]
        protocol = parts[7][:-1]
        status_code = parts[8]
        file_size = parts[9]

        if method != "GET" or endpoint != "/projects/260" or protocol != "HTTP/1.1":
            continue

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print_statistics()

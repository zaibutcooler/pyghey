# Main
from .individuals import print_cross,print_hash,print_line,print_none


def logger_info(message, count=10):
    print_line(count)
    print(f"INFO: {message}")
    print_line(count)

def logger_warn(message, count=10):
    print_hash(count)
    print(f"WARN: {message}")
    print_hash(count)

def logger_error(message, count=10):
    print_cross(count)
    print(f"ERROR: {message}")
    print_cross(count)

def logger_success(message, count=10):
    print_none(count)
    print(f"SUCCESS: {message}")
    print_none(count)
    
    
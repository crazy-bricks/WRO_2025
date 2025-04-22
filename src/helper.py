from config import DEBUG

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def debug_log(*args):
    if DEBUG:
        print(*args)
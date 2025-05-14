from config import DEBUG

def clamp(value, min_value, max_value):
    """
    Clamps a value between a minimum and maximum value.
    
    :param value: Value to clamp
    :param min_value: Minimum value
    :param max_value: Maximum value
    :return: Clamped value
    """
    return max(min(value, max_value), min_value)

def debug_log(*args, name="default"):
    """
    Logs information if in debug mode.

    :param args: Arguments to log
    :return: None
    """
    if DEBUG:
        prefix = "[{}] ".format(name.upper())
        print(prefix, *args)
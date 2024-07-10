class NegativeValueError(Exception):
    pass

def check_value(value):
    if value < 0:
        raise NegativeValueError("Value cannot be negative.")

check_value(-10)

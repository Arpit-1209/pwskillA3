try:
    number = int("invalid")
except ValueError:
    print("ValueError: invalid literal for int()")
finally:
    print("Execution completed.")

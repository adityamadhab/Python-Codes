try:
    value = int("42")
except ValueError as e:
    print("Exception:", e)
else:
    print("No exception occurred. Value is", value)

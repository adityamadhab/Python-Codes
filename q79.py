try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print("Exception:", e)

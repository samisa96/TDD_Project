def IsNumber(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
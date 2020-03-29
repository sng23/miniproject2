def fn_division(a, b):
    if float(b) == 0:
        raise ZeroDivisionError
    else:
        return float(a) / float(b)

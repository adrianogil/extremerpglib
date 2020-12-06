def capitalize(s):
    return s[0].upper() + s[1:]


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        pass

    return False

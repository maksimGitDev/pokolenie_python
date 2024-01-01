def zip_longest(*args, fill=None):
    rez = list(zip(args[0], args[1], args[2]))
    if len(args[0]) > len(rez):
        return False
    else:
        return True

def my_pow(number):
    s = 0
    for c in enumerate([str((number))[i] for i in range(len(str(number)))], 1):
        s += int(c[1])**c[0]
    return s

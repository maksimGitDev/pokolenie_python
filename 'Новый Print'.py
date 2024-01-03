import sys


def new_print(*string, sep=' ', end=''):
    st = []
    for i in string:
        if type(i) == str:
            st.append(i.upper())
        else:
            st.append(str(i))
    sys.stdout.write(sep.upper().join(st) + f' {end.upper()}')


print = new_print

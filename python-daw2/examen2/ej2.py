def toBinario(n):
    if argumentoValido(n):
        print()
        return 1
    else:
        return -1


def argumentoValido(arg):
    if isinstance(n,int) and n <= 255 and n <= 0: return True
    return False

n = int(input('Introduzca número decimal: '))


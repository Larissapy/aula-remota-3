def letra_numero(a):
    if ord(a) <= 47:
        return ('False')
    elif ord(a) <= 57 :
        return ('True')
    elif ord(a) <= 64:
        return ('False')
    elif ord(a) <= 90:
        return ('True')
    elif ord(a) <= 96:
        return ('False')
    elif ord(a) <= 122:
        return ('True')
    else:
        return ('False')

def main():
    l_n = input()

    resultado = letra_numero(l_n)

    print(f'{resultado}')

if __name__ == "__main__":
    main()


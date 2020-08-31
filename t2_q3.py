def consoante(a):
    if a.upper() == 'A':
        return ('False')
    elif a.upper() == 'E':
        return ('False')
    elif a.upper() == 'I':
        return ('False')
    elif a.upper() == 'O':
        return ('False')
    elif a.upper() == 'U':
        return ('False')
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
    c = input('Digite uma consoante: ')

    resultado = consoante(c)

    print(f'A consoante é {resultado}')

if __name__ == "__main__":
        main()

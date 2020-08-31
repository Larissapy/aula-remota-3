def caracteres(a):
    if a.upper() == 'A':
        return ('vogal')
    elif a.upper() == 'E':
        return ('vogal')
    elif a.upper() == 'I':
        return ('vogal')
    elif a.upper() == 'O':
        return ('vogal')
    elif a.upper() == 'U':
        return ('vogal')
    elif ord(a) <= 47:
        return ('símbolo')
    elif ord(a) <= 57 :
        return ('número')
    elif ord(a) <= 64:
        return ('símbolo')
    elif ord(a) <= 90:
        return ('consoante')
    elif ord(a) <= 96:
        return ('símbolo')
    elif ord(a) <= 122:
        return ('consoante')
    else:
        return ('símbolo')

def main():
    c = input('Digite um caractere: ')

    resulta = caracteres(c)

    print(f'O caractere imformado é um(a) {resulta}')

if __name__== "__main__":
    main()

def digito(n):
    if ord(n) <= 47:
        return ('False')
    elif ord(n) <= 57 :
        return ('True')  
    else:
        return ('False') 

def main():

    num = input('Digite um número: ')

    resultado = digito(num)

    print(f'O resultado é {resultado}')

if __name__ == "__main__":
    main()

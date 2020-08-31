def impar(n):
    if n % 2 == 1:
        return ('True')
    else:
        if n % 2 == 0:
            return('False')

def main():
    num = int(input('Digite um número: '))

    resultado = impar(num)

    print(f'O número imformado é um {resultado} ímpar')

if __name__ == "__main__":
    main()

def impar(n):
    if n % 2 == 1:
        return ('True')
    else:
        if n % 2 == 0:
            return('False')

def main():
    num = int(input())

    resultado = impar(num)

    print(f'{resultado}')

if __name__ == "__main__":
    main()

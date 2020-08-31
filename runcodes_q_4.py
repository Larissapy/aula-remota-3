def digito(n):
    if ord(n)<=47:
        return ('False')
    elif ord(n) <= 57 :
        return ('True')  
    else:
        return ('False') 

def main():
    num = input()

    resultado = digito(num)

    print(f'{resultado}')

if __name__ == "__main__":
    main()

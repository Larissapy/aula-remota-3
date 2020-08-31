def letra(a):
    if ord(a) <= 64:
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
    l = input()

    resultado = letra(l)

    print(f'{resultado}')
    
if __name__ == "__main__":
    main()


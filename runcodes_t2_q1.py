def vogal(a):
    if a.upper() == 'A':
        return ('True')
    elif a.upper() == 'E':
        return ('True')
    elif a.upper() == 'I':
        return ('True')
    elif a.upper() == 'O':
        return ('True')
    elif a.upper() == 'U':
        return ('True')
    else:
        return ('False')

def main():
   letra = input()

   resultado = vogal(letra)

   print(f'{resultado}')

if __name__ == "__main__":
    main()
        
        

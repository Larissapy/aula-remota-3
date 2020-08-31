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
   letra = input('Digite uma vogal: ')

   resultado = vogal(letra)

   print(f'A vogal informada é {resultado}')

if __name__ == "__main__":
    main()
        
        

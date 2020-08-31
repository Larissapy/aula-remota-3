def nome_sexo(n,s):
    if s == 1:
        return('Ilmo Sr. ' + n)
    else:
       if s == 2:
            return('Ilma Sra. ' + n)

def main():
    n = input('Qual o seu nome?: ')
    s = int(input('Qual o seu sexo? (1 para masculino e 2 para feminino): '))

    resultado = nome_sexo(n,s)

    print(f'Olá {resultado}')
     
if __name__ == "__main__":
    main()

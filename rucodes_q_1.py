def nome_sexo(n,s):
    if s == 1:
        return('Ilmo Sr. '+ n)
    else:
       if s == 2:
            return('Ilma Sra. ' + n)
  

def main():
    n = input()
    s = int(input())

    resultado = nome_sexo(n,s)

    print(f'{resultado}')
    
if __name__ == "__main__":
    main()

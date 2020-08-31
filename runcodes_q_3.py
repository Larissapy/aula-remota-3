def semaforo(c):
    if c.upper() == 'V':
            return('Siga')
    elif c.upper() == 'A':
        return('Atenção')
    else:
        if c.upper() == 'E':
            return('Pare')
def main():
    c = input()
   
    cor = semaforo(c)

    print(f'{cor}')
    
if __name__ == "__main__":
    main()

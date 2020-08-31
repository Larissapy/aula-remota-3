def semaforo(c):
    if c.upper() == 'V':
            return('Siga')
    elif c.upper() == 'A':
        return('Atenção')
    else:
        if c.upper() == 'E':
            return('Pare')
def main():
    c = input('Imforme a cor do sinal(V para verde A para amarelo e E para vermelho): ')
    
    cor = semaforo(c)

    print(f'O sinal esta em {cor}')
    
if __name__ == "__main__":
    main()

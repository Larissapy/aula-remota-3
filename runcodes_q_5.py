def media_nota(a,b,c):
    media = (a + b + c) / 3
    if c > 8:
        return media + 1
    else:
        return media
def nota_f(r):
    if r > 10:
        return ('10.0')

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    resultado1 = media_nota(n1,n2,n3)

    resultado2 = nota_f(resultado1)
    if resultado2 == '10.0':
        print(f'{resultado2}')
    else:
        if resultado1 <= 10.0:
            print(f'{resultado1}')

if __name__ == "__main__":
    main()

def maiorNumero(num1: float, num2: float) -> float:
    lista = []
    lista.append(num1)
    lista.append(num2)
    return max(lista)


def media(lista: list) -> float:
    return sum(lista)/len(lista)


def numPrimo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5), 1):
        if numero % i == 0:
            return False
    return True


if __name__ == '__main__':
    numero1 = 10
    numero2 = 40

    print(maiorNumero(numero1, numero2))

    numero3 = 7
    print(numPrimo(numero3))

    notas = [7, 3, 10]
    print(media(notas))
'''
escolha = input("[1] para impar ou par\n[2] para media\n")

if escolha == "1":
    res = ("par", "impar")
    num = int(input("Numero: "))
    
    print(f"{num} é {res[num % 2]}")

if escolha == "2":
    soma = 0
    for i in range(0, 3, 1):
        nota = float(input("Nota: "))
        soma += nota
    media = soma / 3
    print(f"Media das notas: {media}")
'''
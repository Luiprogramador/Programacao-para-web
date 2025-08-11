import os
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        valor = float(input("Digite o valor para depósito: "))
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self):
        valor = float(input("Digite o valor para saque: "))
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

class retangolo:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.largura = abs(x2 - x1)
        self.altura = abs(y2 - y1)

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

if __name__ == "__main__":
    titular = input("Digite o nome do titular da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    conta = ContaBancaria(titular, saldo_inicial)

    while True:
        print("\nMenu:")
        print("1. Exibir saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Calcular área e perímetro de um retângulo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conta.exibir_saldo()
        elif opcao == "2":
            conta.depositar()
        elif opcao == "3":
            conta.sacar()
        elif opcao == "4":
            print("\nCalculadora de Retângulo:")
            x1 = float(input("Digite a coordenada x1: "))
            y1 = float(input("Digite a coordenada y1: "))
            x2 = float(input("Digite a coordenada x2: "))
            y2 = float(input("Digite a coordenada y2: "))
            retango = retangolo(x1, y1, x2, y2)

            print(f"Área do retângulo: {retango.area():.2f}")
            print(f"Perímetro do retângulo: {retango.perimetro():.2f}")
        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Opção inválida. Tente novamente.")
        
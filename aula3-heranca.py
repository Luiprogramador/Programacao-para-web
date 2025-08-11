import os

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
    
    def falar(self, mensagem):
        return f"{self.nome} diz: {mensagem}"

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{super().__str__()}, Cargo: {self.cargo}, Salário: {self.salario}"

def criar_objetos():
    tipo = input("Deseja criar uma Pessoa ou um Funcionário? (p/f): ").strip().lower()
    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: ").strip())

    if tipo == 'f':
        cargo = input("Digite o cargo: ").strip()
        salario = float(input("Digite o salário: ").strip())
        return Funcionario(nome, idade, cargo, salario)
    else:
        return Pessoa(nome, idade)

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Criar Objeto")
        print("2. Fazer a pessoa/funcionário falar")
        print("3. Sair")
        opcao = input("Escolha uma opção (1/2): ").strip()

        if opcao == '1':
            objeto = criar_objetos()
            print("\nObjeto criado:")
            print(objeto)
        elif opcao == '2':
            mensagem = input("Digite a mensagem para a pessoa/funcionário falar: ")
            print(objeto.falar(mensagem))
            
        elif opcao == '3':
            print("\nSaindo do programa...")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("\nOpção inválida. Tente novamente.")

        
        
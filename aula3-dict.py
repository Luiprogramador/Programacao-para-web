import os

lista_funcionarios = []
funcionarios = {}
def menu():
    print("\nMenu de Cadastro de Funcionários")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. listar Funcionário pela lista")
    print("4. média de salário dos funcionários")
    print("5. listar funcionários que ganham acima de 5000 reais")
    print("6. Sair")
    return input("Escolha uma opção: ")

def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    idade = input("Digite a idade do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = input("Digite o salário do funcionário: ")
    funcionarios.append({"nome": nome, "idade": idade, "cargo": cargo, "salario": salario})
    print("Funcionário cadastrado com sucesso!")

    lista_funcionarios.append(funcionarios)

def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\nLista de Funcionários:")
        for i, func in enumerate(funcionarios, start=1):
            print(f"{i}. Nome: {func['nome']}, Idade: {func['idade']}, Cargo: {func['cargo']}, Salário: {func['salario']}")
            print("-----------------------------")

def listar_funcionario_pela_lista():
    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\nLista de Funcionários:")
        for i, funcionarios in enumerate(lista_funcionarios, start=1):
            print(f"Lista {i}:")
            for func in funcionarios:
                print(f"Nome: {func['nome']}, Idade: {func['idade']}, Cargo: {func['cargo']}, Salário: {func['salario']}")
                print("-----------------------------")

def calcular_media_salarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    total_salarios = sum(float(func['salario']) for func in funcionarios)
    media_salarios = total_salarios / len(funcionarios)
    print(f"Média de salários dos funcionários: {media_salarios:.2f}")

def listar_funcionarios_acima_de_5000():
    acima_de_5000 = [func for func in funcionarios if float(func['salario']) > 5000]
    if not acima_de_5000:
        print("Nenhum funcionário ganha acima de 5000 reais.")
    else:
        print("\nFuncionários que ganham acima de 5000 reais:")
        for func in acima_de_5000:
            print(f"Nome: {func['nome']}, Salário: {func['salario']}")
            print("-----------------------------")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            listar_funcionario_pela_lista()
        elif opcao == "4":
            calcular_media_salarios()
        elif opcao == "5":
            listar_funcionarios_acima_de_5000()
        elif opcao == "6":
            print("Saindo do programa...")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
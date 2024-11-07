def main_menu():
    while True:
        print("\n--- Bem vindo à database Restaurante, efetue o login para continuar ---")
        print("digite a opção desejada:")
        print("1. logar como administrador ")
        print("2. logar como gerente")
        print("3. logar como funcionário")
        print("4. Sair do programa")
        
        choice = input("Selecione uma opção (1-4): ")

        if choice == '1':
            administrador_menu()
        elif choice == '2':
            gerente_menu()
        elif choice == '3':
            funcionario_menu()
        elif choice == '4':
            print("Saindo do programa")
            break
        else:
            print("Seleção inválida, tente novamente")
            print()

def funcionario_menu():
    while True:
        print("\n--- bem vindo, funcionário! ---")
        print("digite a opção desejada:")
        print("1. Cadastrar novo item")
        print("2. consultar vendas")
        print("3. log-off")
        
        choice = input("Select an option (1-3): ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            print("deslogando")
            main_menu()
            break
        else:
            print("Seleção inválida, tente novamente")

def gerente_menu():
    while True:
        print("\n--- bem vindo, gerente! ---")
        print("digite a opção desejada:")
        print("1. Cadastrar novo item")
        print("2. consultar uma tabela")
        print("3. apagar um registro")
        print("4. editar um registro existente")
        print("5. log-off")
        
        choice = input("Select an option (1-3): ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            print("deslogando")
            main_menu()
            break
        else:
            print("Seleção inválida, tente novamente")

def administrador_menu():
    while True:
        print("\n--- bem vindo, administrador! ---")
        print("digite a opção desejada:")
        print("1. Cadastrar novo item")
        print("2. consultar uma tabela")
        print("3. apagar um registro")
        print("4. editar um registro existente")
        print("6. destruir database")
        print("7. demonstrações de requerimentos")
        print("8. log-off")
        
        choice = input("Selecione uma opção (1-8)): ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            pass
        elif choice == '8':
            print("deslogando")
            main_menu()
            break
        else:
            print("Seleção inválida, tente novamente")

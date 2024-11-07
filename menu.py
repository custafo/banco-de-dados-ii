from sqlalchemy import create_engine, text, URL
from sqlalchemy.exc import SQLAlchemyError, ProgrammingError

from functions import drop_database, create_database
from selects_inserts import *

def main_menu(engine):
    while True:
        print("\n--- Bem vindo à database Restaurante, efetue o login para continuar ---")
        print("digite a opção desejada:")
        print("1. logar como administrador ")
        print("2. logar como gerente")
        print("3. logar como funcionário")
        print("4. Sair do programa")
        
        choice = input("Selecione uma opção (1-4): ")

        if choice == '1':
            administrador_menu(engine)
        elif choice == '2':
            gerente_menu(engine)
        elif choice == '3':
            funcionario_menu(engine)
        elif choice == '4':
            print("Saindo do programa")
            break
        else:
            print("Seleção inválida, tente novamente")
            print()

def funcionario_menu(engine):
    while True:
        print("\n--- bem vindo, funcionário! ---")
        print("digite a opção desejada:")
        print("1. Cadastrar novo item")
        print("2. consultar vendas")
        print("3. log-off")
        
        choice = input("Select an option (1-3): ")

        if choice == '1':
            insert_menu(engine)
        elif choice == '2':
            select_venda(engine)
        elif choice == '3':
            print("deslogando")
            main_menu()
            break
        else:
            print("Seleção inválida, tente novamente")

def gerente_menu(engine):
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
            insert_menu(engine)
        elif choice == '2':
            select_venda(engine)
        elif choice == '3':
            delete_menu(engine)
        elif choice == '4':
            update_menu(engine)
        elif choice == '5':
            print("deslogando")
            main_menu()
            break
        else:
            print("Seleção inválida, tente novamente")

def administrador_menu(engine):
    while True:
        print("\n--- bem vindo, administrador! ---")
        print("digite a opção desejada:")
        print("1. Cadastrar novo item")
        print("2. consultar uma tabela")
        print("3. apagar um registro")
        print("4. editar um registro existente")
        print("5. destruir database")
        print("6. log-off")
        
        choice = input("Selecione uma opção (1-8)): ")

        if choice == '1':
            insert_menu(engine)
        elif choice == '2':
            select_venda(engine)
        elif choice == '3':
            delete_menu(engine)
        elif choice == '4':
            update_menu(engine)
        elif choice == '5':
            drop_database(engine)
        elif choice == '6':
            print("deslogando")
            main_menu()
            break
        else:
            print("Seleção inválida, tente novamente")







def insert_menu(engine):
    while True:
        print("\n--- qual tabela deseja cadastrar? ---")
        print("digite a opção desejada:")
        print("1. Cliente")
        print("2. Prato")
        print("3. Fornecedor")
        print("4. Ingrediente")
        print("5. Usos")
        print("6. Venda")
        print("7. Sair do cadastro")
        
        choice = input("Selecione uma opção (1-8)): ")

        if choice == '1':
            
            nome = input("digite o nome:")
            sexo = input("digite o sexo (apenas 'm', 'f' ou 'o')")
            idade = input("digite a idade:")
            nascimento = input("digite a data de nascimento (formato AAAA-MM-DD):")
            pontos = input("digite os pontos do cliente:")

            insert_cliente(engine, nome, sexo, idade, nascimento, pontos)


        elif choice == '2':
            nome = input("digite o nome do prato:") 
            descricao = input("digite a descrição do prato:")
            valor = input("digite o preço do prato:")
            disponibilidade = 'A'
        
            disponibilidade = input("digite V para disponivel e F para indisponivel:")

            insert_prato(engine, descricao, valor, disponibilidade)

        elif choice == '3':
            nome = input("digite o nome do fornecedor:")
            estado_origem = input("digite apenas a sigla do estado de origem:")

            insert_fornecedor(engine, nome, estado_origem)

        elif choice == '4':
            nome = input("digite o nome do ingrediente:")
            data_fabricacao = input("digite a data de fabricação no modelo AAAA-MM-DD:")
            data_validade = input("digite a data de fabricação no modelo AAAA-MM-DD:")
            quantidade = input("digite a quantidade:")
            observacao = input("digite a descricao do ingrediente:")

            insert_ingrediente(engine, nome, data_fabricacao, data_validade, quantidade, observacao)
			
        elif choice == '5':
            id_prato = input("digite o id do prato:")
            id_ingrediente = input("digite o id do ingrediente:")

            insert_usos(engine, id_prato, id_ingrediente)

        elif choice == '6':
            id_cliente = input("digite id do cliente:")
            id_prato = input("digite id do prato:")
            quantidade = input("digite quantos o cliente pediu:")
            dia = input("digite a data da venda no modelo AAAA-MM-DD:")
            hora = input("digite a hora da venda no modelo HH:MM:")
            valor = input("digite o valor da venda")

            insert_venda(engine, id_cliente, id_prato, quantidade, dia, hora, valor)

        elif choice == '7':
            print("deslogando")
            main_menu()
            break
        else:
            print("Seleção inválida, tente novamente")

def delete_menu(engine):
    while True:
        print("\n--- qual tabela deseja deletar o registro? ---")
        print("digite a opção desejada:")
        print("1. Cliente")
        print("2. Prato")
        print("3. Venda")
        print("4. Ingrediente")
        print("5. Usos")
        print("6. Fornecedor")
        print("7. Sair do cadastro")
        
        choice = input("Selecione uma opção (1-8)): ")

        if choice == '1':
            print("mostrando lista de registros")
            print()
            rows = select_cliente(engine)
            for row in rows:
                print(row)
            print()
            id = input("digite o ID do registro a ser apagado")
            delete_cliente(engine, id)


        elif choice == '2':
            print("mostrando lista de registros")
            print()
            rows = select_prato(engine)
            for row in rows:
                print(row)
            print()
            id = input("digite o ID do registro a ser apagado")
            delete_prato(engine, id)


        elif choice == '3':
            print("mostrando lista de registros")
            print()
            rows = select_ingrediente(engine)
            for row in rows:
                print(row)
            print()
            id = input("digite o ID do registro a ser apagado")
            delete_ingrediente(engine, id)

        elif choice == '4':
            print("mostrando lista de registros")
            print()
            rows = select_usos(engine)
            for row in rows:
                print(row)
            print()
            id_prato = input("digite o primeiro ID do registro a ser apagado (prato)")
            id_ingrediente = input("digite o segundo ID do registro a ser apagado (ingrediente)")
            delete_usos(engine, id_prato, id_ingrediente)

        elif choice == '5':
            print("mostrando lista de registros")
            print()
            rows = select_venda(engine)
            for row in rows:
                print(row)
            print()
            id = input("digite o ID do registro a ser apagado")
            delete_venda(engine, id)


        elif choice == '7':
            print("deslogando")
            main_menu()
            break
        
        else:
            print("Seleção inválida, tente novamente")    

def update_menu(engine):
    while True:
        print("\n--- qual tabela deseja alterar o registro? ---")
        print("digite a opção desejada:")
        print("1. Cliente")
        print("2. Prato")
        print("3. Venda")
        print("4. Ingrediente")
        print("5. Usos")
        print("6. Fornecedor")
        print("7. Sair do cadastro")
        
        choice = input("Selecione uma opção (1-8)): ")

        if choice == '1':
            print("mostrando lista de registros")
            print()
            rows = select_cliente(engine)
            for row in rows:
                print(row)
            print()
            id = input("digite o ID do registro a ser editado")
            nome = input("digite o nome:")
            sexo = input("digite o sexo (apenas 'm', 'f' ou 'o')")
            idade = input("digite a idade:")
            nascimento = input("digite a data de nascimento (formato AAAA-MM-DD):")
            pontos = input("digite os pontos do cliente:")

            update_cliente(engine, id, nome, sexo, idade, nascimento, pontos)


        elif choice == '2':
            print("mostrando lista de registros")
            print()
            rows = select_prato(engine)
            for row in rows:
                print(row)
            print()
            id = input("digite o ID do registro a ser apagado")
            nome = input("digite o nome do prato:") 
            descricao = input("digite a descrição do prato:")
            valor = input("digite o preço do prato:")

            disponibilidade = input("digite V para disponivel e F para indisponivel:")

            update_prato(engine, id, nome, descricao, valor, disponibilidade)


        elif choice == '3':
            print("mostrando lista de registros")
            print()
            rows = select_ingrediente(engine)
            for row in rows:
                print(row)
            print()
            id = input("digite o ID do registro a ser apagado")
            nome = input("digite o nome do ingrediente:")
            data_fabricacao = input("digite a data de fabricação no modelo AAAA-MM-DD:")
            data_validade = input("digite a data de fabricação no modelo AAAA-MM-DD:")
            quantidade = input("digite a quantidade:")
            observacao = input("digite a descricao do ingrediente:")
            update_ingrediente(engine, id, nome, data_fabricacao, data_validade, quantidade, observacao)

        elif choice == '4':
            print("mostrando lista de registros")
            print()
            rows = select_usos(engine)
            for row in rows:
                print(row)
            print()
            id_prato = input("digite o primeiro ID do registro a ser apagado (prato)")
            id_ingrediente = input("digite o segundo ID do registro a ser apagado (ingrediente)")
            update_usos(engine, id_prato, id_ingrediente)

        elif choice == '5':
            print("mostrando lista de registros")
            print()
            rows = select_venda(engine)
            for row in rows:
                print(row)
            print()
            id_cliente = input("digite id do cliente:")
            id_prato = input("digite id do prato:")
            quantidade = input("digite quantos o cliente pediu:")
            dia = input("digite a data da venda no modelo AAAA-MM-DD:")
            hora = input("digite a hora da venda no modelo HH:MM:")
            valor = input("digite o valor da venda")

            update_venda(engine, id_cliente, id_prato, quantidade, dia, hora, valor)

        elif choice == '6':
            print("mostrando lista de registros")
            print()
            rows = select_fornecedor(engine)
            for row in rows:
                print(row)
            print()
            id = input("digite o id do fornecedor:")
            nome = input("digite o nome do fornecedor:")
            estado_origem = input("digite apenas a sigla do estado de origem:")

            update_fornecedor(engine, id, nome, estado_origem)

        elif choice == '7':
            print("deslogando")
            main_menu()
            break
        
        else:
            print("Seleção inválida, tente novamente")    
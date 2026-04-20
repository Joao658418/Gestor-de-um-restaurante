import clientes
import pratos

# Definição do menu
def menu():
    print("\n" + "="*30)
    print("      SISTEMA RESTAURANTE")
    print("="*30)
    print("1 - Criar cliente")
    print("2 - Listar clientes")
    print("3 - Consultar cliente (NIF)")
    print("4 - Atualizar cliente")
    print("5 - Remover cliente")
    print("---")
    print("6 - Criar prato")
    print("7 - Listar pratos")
    print("8 - Consultar prato (ID)")
    print("9 - Atualizar prato")
    print("10 - Remover prato")
    print("0 - Sair")

# Programa principal
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        # --- GESTÃO DE CLIENTES ---
        if opcao == "1":
            nome = input("Nome: ")
            nasc = input("Data Nascimento (YYYY-MM-DD): ")
            nif = input("NIF: ")
            tel = input("Telefone: ")

            code, obj = clientes.adicionar_cliente(nif, nome, nasc, tel)
            if code == 201:
                print("Cliente " + obj["nome"] + " criado com sucesso.")
            else:
                print("Error: " + obj)

        elif opcao == "2":
            code, obj = clientes.listar_clientes()
            if code == 200:
                print("\n--- LISTAGEM DE CLIENTES ---")
                for nif, dados in obj.items():
                    print(f"NIF: {nif} | Nome: {dados['nome']} | Data Nasc: {dados['nascimento']}")
                print("cliente listado com sucesso.")
            else:
                print("Error: " + obj)

        elif opcao == "3":
            nif = input("NIF do utilizador: ")
            code, obj = clientes.pesquisar_cliente(nif)
            if code == 200:
                print(obj)
                print("Cliente listado com sucesso.")
            else:
                print("Error: " + obj)

        elif opcao == "4":
            nif = input("NIF do utilizador: ")
            nome = input("Novo nome (enter para manter): ")
            nasc = input("Nova data (enter para manter): ")
            tel = input("Novo telefone (enter para manter): ")

            code, obj = clientes.atualizar_cliente(
                nif,
                nome if nome else None,
                nasc if nasc else None,
                tel if tel else None
            )
            if code == 200:
                print("cliente actualizado com sucesso.")
            else:
                print("Error: " + obj)

        elif opcao == "5":
            nif = input("NIF do cliente: ")
            code, obj = clientes.remover_cliente(nif)
            if code == 200:
                print("cliente removido com sucesso.")
            else:
                print("Error: " + obj)

        # --- GESTÃO DE PRATOS ---
        elif opcao == "6":
            nome = input("Nome do prato: ")
            preco = input("Preco: ")
            estrelas = input("Estrelas: ")
            tipo = input("Tipo: ")
            ingredientes = input("Ingredientes: ")

            code, obj = pratos.criar_prato(nome, preco, estrelas, tipo, ingredientes)
            if code == 201:
                print("Prato " + obj["nome"] + " criado com sucesso.")
            else:
                print("Error: " + obj)

        elif opcao == "7":
            code, obj = pratos.listar_pratos()
            if code == 200:
                print("\n--- LISTAGEM DE PRATOS ---")
                for p in obj:
                    print(f"ID: {p['id']} | Nome: {p['nome']} | Preco: {p['preco']}")
                print("Pratos listados com sucesso.")
            else:
                print("Error: " + obj)

        elif opcao == "8":
            id_p = input("ID do prato: ")
            code, obj = pratos.consultar_prato(id_p)
            if code == 200:
                print(obj)
                print("Consulta realizada com sucesso.")
            else:
                print("Error: " + obj)

        elif opcao == "9":
            id_p = input("ID do prato: ")
            nome = input("Novo nome (enter para manter): ")
            preco = input("Novo preco (enter para manter): ")

            code, obj = pratos.atualizar_prato(
                id_p,
                nome if nome else None,
                preco if preco else None
            )
            if code == 200:
                print("Prato actualizado com sucesso.")
            else:
                print("Error: " + obj)

        elif opcao == "10":
            id_p = input("ID do prato: ")
            code, obj = pratos.remover_prato(id_p)
            if code == 200:
                print("Prato removido com sucesso.")
            else:
                print("Error: " + obj)

        elif opcao == "0":
            print("A sair...")
            break

        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()

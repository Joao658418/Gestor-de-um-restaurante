import clientes
import pratos

# Definição do menu
def menu():
    print("\n===== MENU CLIENTE =====")
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

        if opcao == "1":
            nif = input("NIF: ")
            nome = input("Nome: ")
            nasc = input("Data Nascimento (YYYY-MM-DD): ")
            tel = input("Telemóvel: ")

            # return_code[0] é o status, return_code[1] é a mensagem
            code, obj = clientes.adicionar_cliente(nif, nome, nasc, tel)

            if code == 201:
                print("Cliente criado com sucesso.")
            elif obj == 500:
                print("Internal Error: " + obj)

        elif opcao == "2":
            code, obj = clientes.listar_clientes()
            # Se for 200, a função listar_clientes já imprimiu a lista
            if return_code[0] == 200:
                print("Clientes listados com sucesso.")
            else:
                print("Internal Error: " + obj)

        elif opcao == "3":
            nif = input("NIF do cliente: ")
            code, obj = clientes.pesquisar_cliente(nif)
            if code == 200:
                print("Consulta realizada com sucesso.")
            else:
                print("Internal Error: " + obj)

        elif opcao == "4":
            nif = input("NIF do cliente: ")
            nome = input("Novo nome (enter para manter): ")
            nasc = input("Nova data (enter para manter): ")
            tel = input("Novo telefone (enter para manter): ")

            # Passamos os dados; se estiver vazio, a lógica no clientes.py ignora
            code, obj = clientes.atualizar_cliente(
                nif,
                nome if nome else None,
                nasc if nasc else None,
                tel if tel else None
            )

            if code == 200:
                print("Cliente atualizado com sucesso.")
            else:
                print("Internal Error: " + obj)

        elif opcao == "5":
            nif = input("NIF do cliente para remover: ")
            code, obj = clientes.remover_cliente(nif)

            if code == 200:
                print("Cliente removido com sucesso.")
            else:
                print("Internal Error: " + obj)

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
                print("Internal Error: " + obj)

        elif opcao == "7":
            code, obj = pratos.listar_pratos()
            if code == 200:
                print("\n--- LISTAGEM DE PRATOS ---")
                for p in obj:
                    print(f"ID: {p['id']} | Nome: {p['nome']} | Preco: {p['preco']}")
                print("Pratos listados com sucesso.")
            else:
                print("Internal Error: " + obj)

        elif opcao == "8":
            id_p = input("ID do prato: ")
            code, obj = pratos.consultar_prato(id_p)
            if code == 200:
                print(obj)
                print("Consulta realizada com sucesso.")
            else:
                print("Internal Error: " + obj)

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
                print("Internal Error: " + obj)

        elif opcao == "10":
            id_p = input("ID do prato: ")
            code, obj = pratos.remover_prato(id_p)
            if code == 200:
                print("Prato removido com sucesso.")
            else:
                print("Internal Error: " + obj)

        elif opcao == "0":
            print("A sair...")
            break

        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()
            print("Opção inválida.")


if __name__ == "__main__":
    main()

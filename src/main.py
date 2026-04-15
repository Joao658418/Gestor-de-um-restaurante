import clientes


# Definição do menu
def menu():
    print("\n===== MENU CLIENTE =====")
    print("1 - Criar cliente")
    print("2 - Listar clientes")
    print("3 - Consultar cliente (NIF)")
    print("4 - Atualizar cliente")
    print("5 - Remover cliente")
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
            return_code = clientes.adicionar_cliente(nif, nome, nasc, tel)

            if return_code[0] == 201:
                print("Cliente criado com sucesso.")
            elif return_code[0] == 500:
                print("Internal Error: " + return_code[1])

        elif opcao == "2":
            return_code = clientes.listar_clientes()
            # Se for 200, a função listar_clientes já imprimiu a lista
            if return_code[0] == 200:
                print("Clientes listados com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "3":
            nif = input("NIF do cliente: ")
            return_code = clientes.pesquisar_cliente(nif)
            if return_code[0] == 200:
                print("Consulta realizada com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "4":
            nif = input("NIF do cliente: ")
            nome = input("Novo nome (enter para manter): ")
            nasc = input("Nova data (enter para manter): ")
            tel = input("Novo telefone (enter para manter): ")

            # Passamos os dados; se estiver vazio, a lógica no clientes.py ignora
            return_code = clientes.atualizar_cliente(
                nif,
                nome if nome else None,
                nasc if nasc else None,
                tel if tel else None
            )

            if return_code[0] == 200:
                print("Cliente atualizado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "5":
            nif = input("NIF do cliente para remover: ")
            return_code = clientes.remover_cliente(nif)

            if return_code[0] == 200:
                print("Cliente removido com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "0":
            print("A sair...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

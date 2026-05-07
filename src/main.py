import clientes
import pratos
import fornecedores
import funcionarios

def menu():
    print("\n" + "="*30)
    print("      SISTEMA RESTAURANTE")
    print("="*30)
    print("1 - Criar cliente      | 6  - Criar prato")
    print("2 - Listar clientes     | 7  - Listar pratos")
    print("3 - Consultar cliente  | 8  - Consultar prato")
    print("4 - Atualizar cliente  | 9  - Atualizar prato")
    print("5 - Remover cliente    | 10 - Remover prato")
    print("-" * 30)
    print("11 - Criar fornecedor  | 16 - Criar funcionario")
    print("12 - Listar fornecedores| 17 - Listar funcionarios")
    print("13 - Consultar fornec. | 18 - Consultar func.")
    print("14 - Atualizar fornec. | 19 - Atualizar func.")
    print("15 - Remover fornec.   | 20 - Remover func.")
    print("0 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        # --- GESTÃO DE CLIENTES (1-5) ---
        if opcao == "1":
            nome = input("Nome: "); nasc = input("Data Nasc: "); nif = input("NIF: "); tel = input("Tel: ")
            code, obj = clientes.adicionar_cliente(nif, nome, nasc, tel)
            if code == 201: print("Cliente " + str(obj["nome"]) + " criado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "2":
            code, obj = clientes.listar_clientes()
            if code == 200:
                for nif, d in obj.items(): print(f"NIF: {nif} | Nome: {d['nome']}")
                print("Utilizador listado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "3":
            nif = input("NIF: "); code, obj = clientes.pesquisar_cliente(nif)
            if code == 200: print(obj); print("Utilizador listado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "4":
            nif = input("NIF: "); nome = input("Novo nome: "); nasc = input("Nova data: "); tel = input("Novo tel: ")
            code, obj = clientes.atualizar_cliente(nif, nome if nome else None, nasc if nasc else None, tel if tel else None)
            if code == 200: print("Utilizador actualizado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "5":
            nif = input("NIF: "); code, obj = clientes.remover_cliente(nif)
            if code == 200: print("Utilizador removido com sucesso.")
            else: print("Internal Error: " + str(obj))

        # --- GESTÃO DE PRATOS (6-10) ---
        elif opcao == "6":
            nome = input("Nome: "); preco = input("Preco: "); est = input("Estrelas: "); tipo = input("Tipo: "); ing = input("Ingredientes: ")
            code, obj = pratos.criar_prato(nome, preco, est, tipo, ing)
            if code == 201: print("Prato " + str(obj["nome"]) + " criado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "7":
            code, obj = pratos.listar_pratos()
            if code == 200:
                for p in obj: print(f"ID: {p['id']} | Nome: {p['nome']} | Preco: {p['preco']}")
                print("Pratos listados com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "8":
            id_p = input("ID: "); code, obj = pratos.consultar_prato(id_p)
            if code == 200: print(obj); print("Consulta realizada com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "9":
            id_p = input("ID: "); nome = input("Novo nome: "); preco = input("Novo preco: ")
            code, obj = pratos.atualizar_prato(id_p, nome if nome else None, preco if preco else None)
            if code == 200: print("Prato actualizado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "10":
            id_p = input("ID: "); code, obj = pratos.remover_prato(id_p)
            if code == 200: print("Prato removido com sucesso.")
            else: print("Internal Error: " + str(obj))

        # --- GESTÃO DE FORNECEDORES (11-15) ---
        elif opcao == "11":
            nome = input("Nome: "); morada = input("Morada: "); tel = input("Tel: "); email = input("Email: "); nif = input("NIF: "); tipo = input("Tipo Produto: ")
            code, obj = fornecedores.criar_fornecedor(nif, nome, morada, tel, email, tipo)
            if code == 201: print("Fornecedor " + str(obj["nome"]) + " criado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "12":
            code, obj = fornecedores.listar_fornecedores()
            if code == 200:
                for nif, d in obj.items(): print(f"NIF: {nif} | Nome: {d['nome']} | Produto: {d['tipo_produto']}")
                print("Fornecedores listados com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "13":
            nif = input("NIF: "); code, obj = fornecedores.consultar_fornecedor(nif)
            if code == 200: print(obj); print("Consulta realizada com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "14":
            nif = input("NIF: "); nome = input("Novo nome: "); tipo = input("Novo tipo produto: ")
            code, obj = fornecedores.atualizar_fornecedor(nif, nome if nome else None, tipo if tipo else None)
            if code == 200: print("Fornecedor actualizado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "15":
            nif = input("NIF: "); code, obj = fornecedores.remover_fornecedor(nif)
            if code == 200: print("Fornecedor removido com sucesso.")
            else: print("Internal Error: " + str(obj))

        # --- GESTÃO DE FUNCIONÁRIOS (16-20) ---
        elif opcao == "16":
            nome = input("Nome: "); nasc = input("Data Nasc: "); nif = input("NIF: "); cargo = input("Cargo: "); sal = input("Salario: "); ent = input("Data Entrada: ")
            code, obj = funcionarios.criar_funcionario(nif, nome, nasc, cargo, sal, ent)
            if code == 201: print("Funcionario " + str(obj["nome"]) + " criado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "17":
            code, obj = funcionarios.listar_funcionarios()
            if code == 200:
                for nif, d in obj.items(): print(f"NIF: {nif} | Nome: {d['nome']} | Cargo: {d['cargo']}")
                print("Funcionarios listados com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "18":
            nif = input("NIF: "); code, obj = funcionarios.consultar_funcionario(nif)
            if code == 200: print(obj); print("Consulta realizada com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "19":
            nif = input("NIF: "); cargo = input("Novo cargo: "); sal = input("Novo salario: "); sai = input("Data Saida (se aplicavel): ")
            code, obj = funcionarios.atualizar_funcionario(nif, cargo if cargo else None, sal if sal else None, sai if sai else None)
            if code == 200: print("Funcionario actualizado com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "20":
            nif = input("NIF: "); code, obj = funcionarios.remover_funcionario(nif)
            if code == 200: print("Funcionario removido com sucesso.")
            else: print("Internal Error: " + str(obj))

        elif opcao == "0":
            print("A sair..."); break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()

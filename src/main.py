import clientes
from utils import db_clientes

def exibir_menu():
    print("\n" + "="*30)
    print("      MENU DE CLIENTES      ")
    print("="*30)
    print("1. Criar Cliente")
    print("2. Listar Clientes")
    print("3. Pesquisar Cliente ")
    print("4. Atualizar Cliente")
    print("5. Remover Cliente")
    print("0. Sair do Programa")
    print("="*30)

# Ciclo infinito para o menu continuar a aparecer até o utilizador digitar 0
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("\n--- NOVO CLIENTE ---")
        nif = input("NIF: ").strip()
        nome = input("Nome: ").strip()
        nasc = input("Data de Nascimento (AAAA-MM-DD): ").strip()
        tel = input("Telemóvel: ").strip()
        
        # Validar se o utilizador não deixou campos vazios importantes
        if nif == "" or nome == "":
            print("\n❌ Erro: NIF e Nome são obrigatórios!")
        else:
            clientes.adicionar_cliente(nif, nome, nasc, tel)

    elif opcao == "2":
        print("\n--- LISTA DE CLIENTES ---")
        if not db_clientes:
            print("Nenhum cliente cadastrado no momento.")
        else:
            for nif, dados in db_clientes.items():
                print(f"NIF: {nif} | Nome: {dados['nome']} | Tel: {dados['telefone']}")

    elif opcao == "3":
        print("\n--- PESQUISAR CLIENTE ---")
        nif = input("Digite o NIF que procura: ").strip()
        resultado = clientes.pesquisar_cliente(nif)
        
        if resultado:
            print(f"\n🔍 Cliente Encontrado:")
            print(f"Nome: {resultado['nome']}")
            print(f"Nascimento: {resultado['nascimento']}")
            print(f"Telemóvel: {resultado['telefone']}")
        else:
            print("\n❌ Cliente com esse NIF não foi encontrado.")

    elif opcao == "4":
        print("\n--- ATUALIZAR CLIENTE ---")
        nif = input("Digite o NIF do cliente que deseja alterar: ").strip()
        
        # Primeiro verificamos se ele existe
        if nif in db_clientes:
            print("Insira os NOVOS dados:")
            novo_nome = input("Novo Nome: ").strip()
            novo_nasc = input("Nova Data de Nascimento: ").strip()
            novo_tel = input("Novo Telemóvel: ").strip()
            
            clientes.atualizar_cliente(nif, novo_nome, novo_nasc, novo_tel)
        else:
            print("\n❌ Cliente não encontrado.")

    elif opcao == "5":
        print("\n--- REMOVER CLIENTE ---")
        nif = input("Digite o NIF do cliente a eliminar: ").strip()
        
        # Confirmação de segurança
        certeza = input(f"Tem a certeza que deseja apagar o NIF {nif}? (s/n): ").strip().lower()
        if certeza == 's':
            clientes.remover_cliente(nif)
        else:
            print("\nOperação cancelada.")

    elif opcao == "0":
        print("\n👋 A fechar o programa... Até à próxima!")
        break # Quebra o ciclo while e encerra o programa
        
    else:
        print("\n⚠️ Opção inválida! Por favor, escolha um número de 0 a 5.")

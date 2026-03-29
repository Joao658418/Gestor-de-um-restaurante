from utils import db_clientes

def adicionar_cliente(nif, nome, nascimento, telefone):
    if nif in db_clientes:
        print(f"\n❌ Erro: O NIF {nif} já existe!")
    else:
        db_clientes[nif] = {
            "nome": nome,
            "nascimento": nascimento,
            "telefone": telefone
        }
        print(f"\n✅ Cliente '{nome}' adicionado com sucesso.")

def atualizar_cliente(nif, novo_nome, novo_nasc, novo_tel):
    if nif in db_clientes:
        db_clientes[nif].update({
            "nome": novo_nome,
            "nascimento": novo_nasc,
            "telefone": novo_tel
        })
        print(f"\n✅ Cliente com NIF {nif} atualizado com sucesso!")
    else:
        print("\n❌ Erro: Cliente não encontrado.")

def remover_cliente(nif):
    if nif in db_clientes:
        # O método pop remove a chave do dicionário
        eliminado = db_clientes.pop(nif)
        print(f"\n🗑️ Cliente '{eliminado['nome']}' removido com sucesso!")
    else:
        print("\n❌ Erro: Cliente não encontrado.")

def pesquisar_cliente(nif):
    # Retorna os dados se encontrar, ou None se não encontrar
    return db_clientes.get(nif, None)

from utils import db_clientes

def adicionar_cliente(nif, nome, nascimento, telefone):
    if nif in db_clientes:
        print(f"Erro: NIF {nif} já existe!")
    else:
        db_clientes[nif] = {
            "nome": nome,
            "nascimento": nascimento,
            "telefone": telefone
        }
        print(f"Cliente {nome} adicionado.")

def atualizar_cliente(nif, novo_nome, novo_nasc, novo_tel):
    if nif in db_clientes:
        db_clientes[nif].update({
            "nome": novo_nome,
            "nascimento": novo_nasc,
            "telefone": novo_tel
        })
        print(f"Cliente {nif} atualizado!")
    else:
        print("Cliente não encontrado.")
from utils import db_clientes


def adicionar_cliente(nif, nome, nascimento, telefone):
    try:
        if not nif or not nome:
            return "NIF e Nome são obrigatórios!", 400

        if nif in db_clientes:
            return "Este NIF já está registado!", 400

        db_clientes[nif] = {
            "nome": nome,
            "nascimento": nascimento,
            "telefone": telefone
        }
        return f"Cliente {nome} criado com sucesso!", 200

    except Exception as e:
        # Se acontecer algum erro bizarro no Python, simulamos o erro 500
        return f"Erro interno do sistema: {e}", 400


def atualizar_cliente(nif, novo_nome, novo_nasc, novo_tel):
    try:
        if nif not in db_clientes:
            return "Cliente não encontrado!", 404

        db_clientes[nif].update({
            "nome": novo_nome,
            "nascimento": novo_nasc,
            "telefone": novo_tel
        })
        return "Cliente atualizado com sucesso!", 200

    except Exception as e:
        return f"Erro interno: {e}", 400


def remover_cliente(nif):
    try:
        if nif not in db_clientes:
            return 404, "Cliente não encontrado!"

        eliminado = db_clientes.pop(nif)
        return 200, nif

    except Exception as e:
        return f"Erro interno: {e}", 500


def pesquisar_cliente(nif):
    try:
        if nif in db_clientes:
            return db_clientes[nif], 200
        return "Cliente não encontrado!", 404

    except Exception as e:
        return f"Erro interno: {e}", 500


def listar_clientes():
    if not db_clientes:
        print("\n[HTTP 404] Não existem clientes registados.")
        return 404, "Não existem clientes registados."

    print("\n--- LISTAGEM DE CLIENTES ---")
    for nif, dados in db_clientes.items():
        print(f"NIF: {nif} | Nome: {dados['nome']} | Data Nasc: {dados['nascimento']} | Tel: {dados['telefone']}")

    return 200, "Sucesso"

from utils import db_clientes


def adicionar_cliente(nif, nome, nascimento, telefone):
    try:
        if not nif or not nome:
            return 400, "NIF e Nome são obrigatórios!"

        if nif in db_clientes:
            return 400, "Este NIF já está registado!"
        cliente = {
            "nome": nome,
            "nascimento": nascimento,
            "telefone": telefone,
            "nif": nif
        }
        db_clientes[nif] = cliente
        return 201, cliente

    except Exception as e:
        # Se acontecer algum erro bizarro no Python, simulamos o erro 500
        return 400, f"Erro interno do sistema: {e}"


def atualizar_cliente(nif, novo_nome, novo_nasc, novo_tel):
    try:
        if nif not in db_clientes:
            return 404,  "Cliente não encontrado!"
        cliente = {
            "nome": novo_nome,
            "nascimento": novo_nasc,
            "telefone": novo_tel,
            "nif": nif
        }
        db_clientes[nif].update(cliente)
        return 200, cliente

    except Exception as e:
        return 400,"Erro interno: {e}"


def remover_cliente(nif):
    try:
        if nif not in db_clientes:
            return 404, "Cliente não encontrado!"

        cliente_eliminado = db_clientes.pop(nif)
        return 200, cliente_eliminado

    except Exception as e:
        return 500, f"Erro interno: {e}"


def pesquisar_cliente(nif):
    try:
        if nif in db_clientes:
            return 200, db_clientes[nif]
        return 404,"Cliente não encontrado!",

    except Exception as e:
        return 500, "Erro interno: {e}"


def listar_clientes():
    if not db_clientes:
        print("\n[HTTP 404] Não existem clientes registados.")
        return 404, "Não existem clientes registados."

    print("\n--- LISTAGEM DE CLIENTES ---")
    for nif, dados in db_clientes.items():
        print(f"NIF: {nif} | Nome: {dados['nome']} | Data Nasc: {dados['nascimento']} | Tel: {dados['telefone']}")

    return 200, "Sucesso"

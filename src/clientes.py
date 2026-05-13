import json
import os

FICHEIRO_CLIENTES = "clientes.json"
db_clientes = {} # Mantive o nome que tinhas no utils

def guardar():
    with open(FICHEIRO_CLIENTES, "w", encoding="utf-8") as f:
        json.dump(db_clientes, f, indent=4, ensure_ascii=False)

def carregar():
    global db_clientes
    if os.path.exists(FICHEIRO_CLIENTES):
        with open(FICHEIRO_CLIENTES, "r", encoding="utf-8") as f:
            db_clientes = json.load(f)

def adicionar_cliente(nif, nome, nascimento, telefone):
    carregar()
    if nif in db_clientes:
        return 400, "Cliente ja existe."
    cliente = {"nome": nome, "nascimento": nascimento, "telefone": telefone}
    db_clientes[nif] = cliente
    guardar()
    return 201, cliente

def listar_clientes():
    carregar()
    if not db_clientes:
        return 404, "Nao existem clientes registados."
    return 200, db_clientes

def pesquisar_cliente(nif):
    carregar()
    if nif not in db_clientes:
        return 404, "Nao encontrado."
    return 200, db_clientes[nif]

def atualizar_cliente(nif, nome=None, nascimento=None, telefone=None):
    carregar()
    if nif not in db_clientes:
        return 404, "Nao encontrado."
    if nome: db_clientes[nif]["nome"] = nome
    if nascimento: db_clientes[nif]["nascimento"] = nascimento
    if telefone: db_clientes[nif]["telefone"] = telefone
    guardar()
    return 200, db_clientes[nif]

def remover_cliente(nif):
    carregar()
    if nif in db_clientes:
        removido = db_clientes.pop(nif)
        guardar()
        return 200, removido
    return 404, "Nao encontrado."

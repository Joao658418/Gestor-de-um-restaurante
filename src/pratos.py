import json
import os

FICHEIRO_PRATOS = "pratos.json"
db_pratos = {}

def guardar():
    with open(FICHEIRO_PRATOS, "w", encoding="utf-8") as f:
        json.dump(db_pratos, f, indent=4, ensure_ascii=False)

def carregar():
    global db_pratos
    if os.path.exists(FICHEIRO_PRATOS):
        with open(FICHEIRO_PRATOS, "r", encoding="utf-8") as f:
            db_pratos = json.load(f)

def criar_prato(nome, preco, estrelas, tipo, ingredientes):
    carregar()
    novo_id = str(len(db_pratos) + 1)
    prato = {"id": novo_id, "nome": nome, "preco": preco, "estrelas": estrelas, "tipo": tipo, "ingredientes": ingredientes}
    db_pratos[novo_id] = prato
    guardar()
    return 201, prato

def listar_pratos():
    carregar()
    if not db_pratos:
        return 404, "Nao existem pratos."
    return 200, list(db_pratos.values())

def consultar_prato(id_prato):
    carregar()
    if id_prato not in db_pratos:
        return 404, "Nao encontrado."
    return 200, db_pratos[id_prato]

def atualizar_prato(id_prato, nome=None, preco=None):
    carregar()
    if id_prato not in db_pratos:
        return 404, "Nao encontrado."
    if nome: db_pratos[id_prato]["nome"] = nome
    if preco: db_pratos[id_prato]["preco"] = preco
    guardar()
    return 200, db_pratos[id_prato]

def remover_prato(id_prato):
    carregar()
    if id_prato in db_pratos:
        removido = db_pratos.pop(id_prato)
        guardar()
        return 200, removido
    return 404, "Nao encontrado."

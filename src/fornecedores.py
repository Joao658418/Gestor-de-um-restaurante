import json
import os

FICHEIRO_FORNECEDORES = "fornecedores.json"
db_fornecedores = {}

def guardar():
    with open(FICHEIRO_FORNECEDORES, "w", encoding="utf-8") as f:
        json.dump(db_fornecedores, f, indent=4, ensure_ascii=False)

def carregar():
    global db_fornecedores
    if os.path.exists(FICHEIRO_FORNECEDORES):
        with open(FICHEIRO_FORNECEDORES, "r", encoding="utf-8") as f:
            db_fornecedores = json.load(f)

def criar_fornecedor(nif, nome, morada, tel, email, tipo_produto):
    carregar()
    if nif in db_fornecedores:
        return 400, "Fornecedor ja existe."
    fornecedor = {"nome": nome, "morada": morada, "telefone": tel, "email": email, "tipo_produto": tipo_produto}
    db_fornecedores[nif] = fornecedor
    guardar()
    return 201, fornecedor

def listar_fornecedores():
    carregar()
    if not db_fornecedores:
        return 404, "Nao existem fornecedores."
    return 200, db_fornecedores

def consultar_fornecedor(nif):
    carregar()
    if nif in db_fornecedores:
        return 200, db_fornecedores[nif]
    return 404, "Nao encontrado."

def atualizar_fornecedor(nif, nome=None, tipo_produto=None):
    carregar()
    if nif not in db_fornecedores:
        return 404, "Nao encontrado."
    if nome: db_fornecedores[nif]["nome"] = nome
    if tipo_produto: db_fornecedores[nif]["tipo_produto"] = tipo_produto
    guardar()
    return 200, db_fornecedores[nif]

def remover_fornecedor(nif):
    carregar()
    if nif in db_fornecedores:
        removido = db_fornecedores.pop(nif)
        guardar()
        return 200, removido
    return 404, "Nao encontrado."

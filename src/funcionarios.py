import json
import os

FICHEIRO_FUNCIONARIOS = "funcionarios.json"
db_funcionarios = {}

def guardar():
    with open(FICHEIRO_FUNCIONARIOS, "w", encoding="utf-8") as f:
        json.dump(db_funcionarios, f, indent=4, ensure_ascii=False)

def carregar():
    global db_funcionarios
    if os.path.exists(FICHEIRO_FUNCIONARIOS):
        with open(FICHEIRO_FUNCIONARIOS, "r", encoding="utf-8") as f:
            db_funcionarios = json.load(f)

def criar_funcionario(nif, nome, nascimento, cargo, salario, data_entrada):
    carregar()
    if nif in db_funcionarios:
        return 400, "Funcionario ja existe."
    funcionario = {"nome": nome, "nascimento": nascimento, "cargo": cargo, "salario": salario, "data_entrada": data_entrada, "data_saida": None}
    db_funcionarios[nif] = funcionario
    guardar()
    return 201, funcionario

def listar_funcionarios():
    carregar()
    if not db_funcionarios:
        return 404, "Nao existem funcionarios."
    return 200, db_funcionarios

def consultar_funcionario(nif):
    carregar()
    if nif in db_funcionarios:
        return 200, db_funcionarios[nif]
    return 404, "Nao encontrado."

def atualizar_funcionario(nif, cargo=None, salario=None, data_saida=None):
    carregar()
    if nif not in db_funcionarios:
        return 404, "Nao encontrado."
    if cargo: db_funcionarios[nif]["cargo"] = cargo
    if salario: db_funcionarios[nif]["salario"] = salario
    if data_saida: db_funcionarios[nif]["data_saida"] = data_saida
    guardar()
    return 200, db_funcionarios[nif]

def remover_funcionario(nif):
    carregar()
    if nif in db_funcionarios:
        removido = db_funcionarios.pop(nif)
        guardar()
        return 200, removido
    return 404, "Nao encontrado."

from utils import db_funcionarios


def criar_funcionario(nif, nome, nascimento, cargo, salario, data_entrada):
    try:
        if not nif or not nome:
            return 400, "NIF e Nome sao obrigatorios."

        if nif in db_funcionarios:
            return 400, "Funcionario ja existe."

        db_funcionarios[nif] = {
            "nome": nome,
            "nascimento": nascimento,
            "cargo": cargo,
            "salario": salario,
            "data_entrada": data_entrada,
            "data_saida": None  # Inicialmente vazio
        }
        return 201, db_funcionarios[nif]
    except Exception as e:
        return 500, str(e)


def listar_funcionarios():
    if not db_funcionarios:
        return 404, "Nao existem funcionarios registados."
    return 200, db_funcionarios


def consultar_funcionario(nif):
    if nif in db_funcionarios:
        return 200, db_funcionarios[nif]
    return 404, "Funcionario nao encontrado."


def atualizar_funcionario(nif, cargo=None, salario=None, data_saida=None):
    if nif not in db_funcionarios:
        return 404, "Funcionario nao encontrado."

    if cargo: db_funcionarios[nif]["cargo"] = cargo
    if salario: db_funcionarios[nif]["salario"] = salario
    if data_saida: db_funcionarios[nif]["data_saida"] = data_saida

    return 200, db_funcionarios


def remover_funcionario(nif):
    if nif in db_funcionarios:
        db_funcionarios.pop(nif)
        return 200, db_funcionarios
    return 404, "Funcionario nao encontrado."

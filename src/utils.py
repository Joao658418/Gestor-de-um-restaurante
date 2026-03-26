# Listas e Dicionários globais que funcionam como nosso Banco de Dados
db_clientes = {}  # Usamos dicionário: {NIF: {dados}}
db_pratos = []    # Usamos lista: [{dados}, {dados}]

def limpar_dados():
    global db_clientes, db_pratos
    db_clientes.clear()
    db_pratos.clear()
    print("Dados limpos com sucesso!")
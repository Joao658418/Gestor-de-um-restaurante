import clientes
import pratos
from utils import db_clientes, db_pratos

# --- TESTE: ADICIONAR ---
clientes.adicionar_cliente("123456789", "João Souza", "2009-10-10", "961234567")
pratos.adicionar_prato("Hambúrguer", 8.50, 4, "Lanche", "Pão, Carne, Queijo")

# --- TESTE: ATUALIZAR TUDO ---
print("\n--- REALIZANDO ATUALIZAÇÕES ---")
clientes.atualizar_cliente("123456789", "Carlos Alberto Silva", "1990-10-10", "969999999")
pratos.atualizar_prato(1, "Super Hambúrguer", 10.00, 5, "Lanche", "Pão, Carne, Queijo, Bacon, Ovo")

# --- MOSTRAR RESULTADOS FINAIS ---
print("\n--- LISTA DE CLIENTES  ---")
for nif, c in db_clientes.items():
    print(f"NIF: {nif} | Nome: {c['nome']} | Tel: {c['telefone']}")

print("\n--- CARDÁPIO ---")
for p in db_pratos:
    ing = ", ".join(p['ingredientes'])
    print(f"ID: {p['id']} | {p['nome']} | {p['preco']}€ | Tipo: {p['tipo']}")
    print(f"Ingredientes: {ing}")

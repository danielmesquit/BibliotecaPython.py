from cliente.cliente_banco import clientes

id_atual = 1

def gerarCliente(nome: str, idade: int):
    global id_atual  # alterar valor de variavel global
    id_atual += 1
    cliente = {
        'nome': nome,
        'idade': idade,
        'status': 'ativo'
    }
    return cliente

def registrarCliente(nome: str, idade: int):

    cliente = gerarCliente(nome,idade)

    clientes.append(cliente)

    print(f"Cliente {cliente['nome']} cadastrado com sucesso")

if __name__ == "__main__":
    registrarCliente("Pedra", 26)
    print(clientes)
from cliente.cliente_banco import clientes
from cliente.buscar_cliente import buscarCliente

def deletarCliente(id: int) -> dict or None:
    cliente = buscarCliente(id)
    for cliente in clientes:
        if cliente['id'] == id:
            clientes.remove(cliente)
            print('Cliente removido com sucesso!')
        else:
            print("Erro: Cliente não encontrado!")

if __name__ == '__main__':
    print(clientes)
    deletarCliente(1)
    print(clientes)
    deletarCliente(5)
from cliente.cliente_banco import clientes
from cliente.buscar_cliente import buscarCliente

def editarCliente(id: int,nome: str, idade: int, status: str):
    cliente = buscarCliente(id)

    if cliente:
        cliente['nome'] = nome
        cliente['idade'] = idade
        cliente['status'] = status

        print(f"Cliente alterado com sucesso!\n")
        print(f"Id: {cliente['id']}")
        print(f"Titulo: {cliente['nome']}")
        print(f"Idade: {cliente['idade']}")
        print(f"Status: {cliente['status']}")
        print("*" * 50)
        return
    print("Erro: cliente não encontrado!")

def editarStatuscliente(id: int, disponivel: bool):
    cliente = buscarCliente(id)

    if cliente:
        cliente['disponivel'] = disponivel

        print("O status foi alterado com sucesso!")

        if disponivel == True:
            print(f"Agora o cliente {cliente['nome']} está disponível.")
        else:
            print(f"O cliente {cliente['nome']} está indisponível no momento.")
        return
    print("Erro: Cliente não encontrado!")


if __name__ == '__main__':
    print(clientes)
    cliente = editarCliente(1,"Bolinha",89, 'Inativo')
    print(clientes)
from cliente.cliente_banco import clientes
from livro.livro_repositorio import livros

def listarClientes():
    print('--- Lista de Livros ---')
    for cliente in clientes:
        print(f"Id: {cliente['id']}")
        print(f"Nome: {cliente['nome']}")
        print(f"idade: {cliente['idade']}")
        if len(cliente['livro']) < 0 :
            for livro in cliente:
                print(f"Id: {livro['id']}")
                print(f"Titulo: {livro['titulo']}")
                print(f"Editora: {livro['editora']}")
                print(f"Status: {livro['disponivel']}")
        else:
            print(f"Livro: {cliente['livro']}")
        print(f"Status: {cliente['status']}")
        print("*"*50)


if __name__ == "__main__":
    listarClientes()
from livro.livro_repositorio import livros
from livro.buscar_livro import buscarLivro
from cliente.cliente_banco import clientes
from cliente.buscar_cliente import buscarCliente

def emprestarLivro(id: int, clienteId):
    livro = buscarLivro(id)
    cliente = buscarCliente(clienteId)

    if not livro:
        print("Erro: Livro não encontrado!")
        return

    if not livro['disponivel']:
        print(f"O livro {livro['titulo']} está indisponível.")
        return

    if not cliente:
        print("Erro: Cliente não encontrado!")
        return

    livro['disponivel'] = False
    cliente['livros'].append(livro)

    print(f"Emprestimo do livro {livro['titulo']} realizado com sucesso!")



if __name__ == "__main__":
    emprestarLivro(1,1)
    print(livros)
    print(clientes)

def devolverLivro(id: int):
    livro = buscarLivro(id)
    if not livro:
        print("Erro: Livro não encontrado!")
        return
    if livro['disponivel']:
        print(f"Erro: O livro {livro['titulo']} já está disponível.")
        return
    livro['disponivel'] = True
    print(f"O livro {livro['titulo']} foi devolvido com sucesso!")

if __name__ == "__main__":
    devolverLivro(1)
    print(livros)
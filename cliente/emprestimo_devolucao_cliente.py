from cliente.cliente_banco import clientes
from cliente.buscar_cliente import buscarCliente
from livro.livro_repositorio import livros
from livro.buscar_livro import buscarLivro
from livro.emprestimo_devolucao_livro import emprestarLivro, devolverLivro

def alugarLivro(clienteId: int, livroId: int):
    livro = buscarLivro(livroId)
    cliente = buscarCliente(clienteId)

    if not livro:
        print('Erro: Livro não encontrado')

    else:
        if not cliente:
            print('Erro: Livro não encontrado')

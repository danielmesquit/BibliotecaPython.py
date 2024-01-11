from livro.livro_repositorio import livros
from livro.buscar_livro import buscarLivro

def editarLivro(id: int,titulo: str, editora: str, disponivel: bool):
    livro = buscarLivro(id)

    if livro:
        livro['titulo'] = titulo
        livro['editora'] = editora
        livro['disponivel'] = disponivel

        print(f"Livro alterado com sucesso!\n")
        print(f"Id: {livro['id']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Editora: {livro['editora']}")
        print(f"Status: {livro['disponivel']}")
        print("*" * 50)
        return
    print("Erro: Livro não encontrado!")

def editarStatusLivro(id: int, disponivel: bool):
    livro = buscarLivro(id)

    if livro:
        livro['disponivel'] = disponivel

        print("O status foi alterado com sucesso!")

        if disponivel == True:
            print(f"Agora o livro {livro['titulo']} está disponível.")
        else:
            print(f"O livro {livro['titulo']} está indisponível no momento.")
        return
    print("Erro: Livro não encontrado!")




if __name__ == '__main__':
    print(livros)
    livro = editarLivro(1,"Bolinha","Alamo", False)
    print(livros)


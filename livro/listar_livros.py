from livro.livro_repositorio import livros
# from livro.registrar import registrarLivro, gerarLivro

def listarLivros():
    print('--- Lista de Livros ---')
    for livro in livros:
        print(f"Id: {livro['id']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Editora: {livro['editora']}")
        print(f"Status: {livro['disponivel']}")
        print("*"*50)


# if __name__ == "__main__":
#     registrarLivro("Deu Certo", "Vamo")
#     print(livros)


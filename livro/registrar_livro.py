from livro.livro_repositorio import livros

id_atual = 1

def gerarLivro(titulo: str, editora: str):
    global id_atual  # alterar valor de variavel global
    id_atual += 1
    livro = {
        "id": id_atual,
        "titulo": titulo,
        "editora": editora,
        "disponivel": True
    }
    return livro

def registrarLivro(titulo: str, editora: str):

    livro = gerarLivro(titulo, editora)

    livros.append(livro)

    print(f"Livro {livro['titulo']} cadastrado com sucesso")

# if __name__ == "__main__":
#     registrarLivro("Deu Certo", "Vamo")
#     print(livros)
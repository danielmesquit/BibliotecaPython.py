from livro.livro_repositorio import livros
from livro.registrar_livro import registrarLivro
from livro.listar_livros import listarLivros
from livro.buscar_livro import buscarLivro
from livro.editar_livro import editarLivro
from livro.deletar_livro import deletarLivro

def menuBiblioteca():
    while True:
        print('--- Menu Biblioteca ---')
        print('--- 1 - Cadastrar Livro ---')
        print('--- 2 - Editar Livro ---')
        print('--- 3 - Remover Livro ---')
        print('--- 4 - Buscar Livro ---')
        print('--- 5-  Listar todos os livro ---')
        print('--- 6-  Sair ---')

        opcao = int(input('Selecione uma opção: '))

        if opcao == 1:
            titulo = input("Digite o nome do livro:")
            editora = input("Digite a editora do livro:")
            registrarLivro(titulo, editora)

        elif opcao == 2:
            id = int(input("Digite o id do livro: "))
            titulo = input("Digite o nome do livro:")
            editora = input("Digite a editora do livro:")
            disponibilidade = int(input('Digite 1 para disponível e 2 para indisponível: '))

            if disponibilidade == 1:
                disponivel = True
            else:
                disponivel = False

            editarLivro(id, titulo, editora, disponivel)

        elif opcao == 3:
            id = int(input("Digite o id do livro: "))
            deletarLivro(id)

        elif opcao == 4:
            id = int(input("Digite o id do livro: "))
            print(buscarLivro(id))

        elif opcao == 5:
            listarLivros()

        elif opcao == 6:
            break

        else:
            print('Opção inválida! Digite um número válido!')

menuBiblioteca()
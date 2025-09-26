from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario
from dados import Dados
import usuario 

def menu():
    biblioteca = Biblioteca()  

    while True:
        print("""
        #========📚 Menu Principal 📚========#
        1 - Adicionar Usuário
        2 - Remover Usuário
        3 - Buscar Usuário
        4 - Exibir Usuário
        5 - Adicionar Livro
        6 - Remover Livro
        7 - Buscar Livro
        8 - Exibir Livros
        9 - Emprestar Livro
        10 - Devolver Livro
        #====================================#
        """)
        
        opition = input("Escolha uma opção no menu acima: ")

        if opition == "1":
            print("\n===📋 Adição de Usuário 📋===")
            nome = input("Nome: ")
            cpf = input("CPF (apenas números): ")
            senha = input("Senha: ")

            resultado = biblioteca.adicionar_usuario(nome, cpf, senha)
            if resultado is True:
                print("Usuário cadastrado com sucesso!")
            else:
                print(f"{resultado}")

        elif opition == "2":
            print("\n===📋 Cadastro de Livro 📋===")
            titulo = input("Título: ")
            ano = input("Ano: ")
            autor = input("Autor: ")
            genero = input("Gênero: ")

            livro = Livro(titulo, ano, autor, genero)
            biblioteca.livros.append(livro)
            print("\n Livro cadastrado com sucesso!")

        elif opition == "3":
            print("\n=== Lista de Usuários ===")
            biblioteca.exibir_usuarios()

        elif opition == "4":
            print("\n===📕Lista de Livros📕===")
            if biblioteca.livros:
                for l in biblioteca.livros:
                    print(f"Título: {l.titulo} | Autor: {l.autor} | Ano: {l.ano} | Gênero: {l.genero} | Disponível: {l.disponivel}")
            else:
                print("\n Nenhum livro cadastrado!")

        elif opition == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":

    menu()

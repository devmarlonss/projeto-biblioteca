from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario
from dados import Dados

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
        11 - Sair
        #====================================#
        """)
        
        opition = input("Escolha uma opção no menu acima: ")

        if opition == "1":
            print("\n===📋 Adição de Usuário 📋===")
            nome = input("Nome: ")
            cpf = input("CPF (apenas números): ")
            senha = input("Senha: ")

            resultado = biblioteca.adicionar_usuario(nome, cpf, senha)
            print(f"Usuário cadastrado com sucesso!" if resultado else resultado)

        elif opition == "2":
            print("\n===❌Remover Usuário❌===")
            cpf = input("insira o CPF para a remoção do usuário: ")
            resultado = biblioteca.remover_usuario(cpf)
            print(f"Usuário removido com sucesso!" if resultado else "Não foi possível remover o usuário!")

        elif opition == "3":
            print("\n===🔎Buscar Usuário🔍===")
            cpf = input("insira o CPF para buscar o usuário: ")
            resultado = biblioteca.buscar_usuario(cpf)
            if not resultado:
                print("Usuário não encontrado!")
            else:
                print(f"Nome: {resultado[0]} | CPF: {resultado[1]}")

        elif opition == "4":
            print("\n===📑Exibir Usuários📑===")
            biblioteca.exibir_usuarios()

        elif opition == "5":
            print("\n===📋 Adição de Livro 📋===")
            titulo = input("Título: ")
            ano = input("Ano: ")
            autor = input("Autor: ")
            genero = input("Gênero: ")
            resultado = biblioteca.adicionar_livro(titulo, ano, autor, genero)
            print("Livro adicionado com sucesso!" if resultado else resultado)

        elif opition == "6":
            print("\n===❌Remoção de Livro❌===")
            titulo = input("insira o título para a remoção do livro: ")
            resultado = biblioteca.remover_livro(titulo)
            print(f"Livro removido com sucesso!" if resultado else "Não foi possível remover o Livro!")

        elif opition == "7":
            print("\n===🔎Buscar Usuário🔍===")
            titulo = input("insira o título para buscar o livro: ")
            resultado = biblioteca.buscar_livro(titulo)
            if not resultado:
                print("Livro não encontrado!")
            else:
                print(f"titulo: {resultado[0]} | autor: {resultado[1]} | ano: {resultado[2]} | genero: {resultado[3]} | disponivel: {resultado[4]}")

        elif opition == "8":
            print("\n===📖Exibir Livros📖===")
            biblioteca.exibir_livros()

        elif opition == "9":
            print("\n===📗Emprestar Livros📗===")
            titulo = input("Informe o título do livro: ")
            cpf = input("Informe o cpf:")
            senha = input("Informe a senha:")
            resultado = biblioteca.emprestar_livros(titulo, cpf, senha)
            print(f"Livro emprestrado com sucesso!" if resultado else resultado)

        elif opition == "10":
            print("\n===📕Devolver Livro📕===")
            titulo = input("Informe o título do livro: ")
            cpf = input("Informe o cpf:")
            senha = input("Informe a senha:")
            resultado = biblioteca.devolver_livros(titulo, cpf, senha)
            print(f"Livro devolvido com sucesso!" if resultado else resultado)
        
        elif opition == "11":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":

    menu()

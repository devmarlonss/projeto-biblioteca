from biblioteca import Biblioteca

def menu():
    biblioteca = Biblioteca()
    biblioteca.carregar_usuarios()
    biblioteca.carregar_livros()

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
        11 - Ver livros emprestados ao usuário      
        12 - Ver histórico de livros do usuário
        13 - Sair
        #====================================#
        """)
        
        option = str(input("Escolha uma opção no menu acima: "))

        if option == "1":
            print("\n===📋 Adição de Usuário 📋===")
            nome = input("Nome: ")
            cpf = input("CPF (apenas números): ")
            senha = input("Senha: ")

            resultado = biblioteca.adicionar_usuario(nome, cpf, senha)
            print(f"\nUsuário cadastrado com sucesso!" if resultado == True else resultado)

        elif option == "2":
            print("\n===❌Remover Usuário❌===")
            cpf = input("insira o CPF para a remoção do usuário: ")
            resultado = biblioteca.remover_usuario(cpf)
            print(f"Usuário removido com sucesso!" if resultado == True else "Não foi possível remover o usuário!")

        elif option == "3":
            print("\n===🔎Buscar Usuário🔍===")
            cpf = input("insira o CPF para buscar o usuário: ")
            resultado = biblioteca.buscar_usuario(cpf)
            if not resultado:
                print("\nUsuário não encontrado!")
            else:
                print(f"\nNome: {resultado[0]} | CPF: {resultado[1]}")

        elif option == "4":
            print("\n===📑Exibir Usuários📑===")
            biblioteca.exibir_usuarios()

        elif option == "5":
            print("\n===📋 Adição de Livro 📋===")
            titulo = input("Título: ")
            ano = input("Ano: ")
            autor = input("Autor: ")
            genero = input("Gênero: ")
            resultado = biblioteca.adicionar_livro(titulo, ano, autor, genero)
            print("\nLivro adicionado com sucesso!" if resultado == True else resultado)

        elif option == "6":
            print("\n===❌Remoção de Livro❌===")
            titulo = input("insira o título para a remoção do livro: ")
            resultado = biblioteca.remover_livro(titulo)
            print(f"Livro removido com sucesso!" if resultado == True else "Não foi possível remover o Livro!")

        elif option == "7":
            print("\n===🔎Buscar Usuário🔍===")
            titulo = input("insira o título para buscar o livro: ")
            resultado = biblioteca.buscar_livro(titulo)
            if not resultado:
                print("\nLivro não encontrado!")
            else:
                print(f"titulo: {resultado[0]} | autor: {resultado[1]} | ano: {resultado[2]} | genero: {resultado[3]} | disponivel: {resultado[4]}")

        elif option == "8":
            print("\n===📖Exibir Livros📖===")
            biblioteca.exibir_livros()

        elif option == "9":
            print("\n===📗Emprestar Livros📗===")
            titulo = input("Informe o título do livro: ")
            cpf = input("Informe o CPF: ")
            senha = input("Informe a senha: ")
            resultado = biblioteca.emprestar_livros(titulo, cpf, senha)
            print(f"\nLivro emprestrado com sucesso!" if resultado == True else resultado)

        elif option == "10":
            print("\n===📕Devolver Livro📕===")
            titulo = input("Informe o título do livro: ")
            cpf = input("Informe o CPF: ")
            senha = input("Informe a senha:")
            resultado = biblioteca.devolver_livros(titulo, cpf, senha)
            print(f"\nLivro devolvido com sucesso!" if resultado == True else resultado)

        elif option == "11":
            print("\n===📚Livros Emprestados📚===")
            cpf = input("Informe o CPF: ")
            resultado = biblioteca.ver_emprestimos(cpf)
            print(f"\n" if resultado == True else resultado)

        elif option == "12":
            print("\n===📚Históricos de Livros📚===")
            cpf = input("Informe o CPF: ")
            resultado = biblioteca.ver_historico(cpf)
            print(f"\n" if resultado == True else resultado)
        
        elif option == "13":
            biblioteca.salvar_usuarios()
            biblioteca.salvar_livros()
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":

    menu()

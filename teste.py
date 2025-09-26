from biblioteca import Biblioteca

# Criando a instância da Biblioteca
b = Biblioteca()

# Teste 1 - Adicionar Usuário
print("Teste 1 - Adicionar Usuário:")
print(b.adicionar_usuario("Marlon", "12345678901", "1234"))  # True
print(b.adicionar_usuario("Marlon", "12345678901", "1234"))  # USUÁRIO JÁ CADASTRADO!
print(b.adicionar_usuario("João", "abc", "1234"))  # CPF INVÁLIDO!
print()

# Teste 2 - Buscar Usuário
print("Teste 2 - Buscar Usuário:")
print(b.buscar_usuario("12345678901"))  # ("Marlon", "12345678901")
print(b.buscar_usuario("00000000000"))  # False
print()

# Teste 3 - Adicionar Livro
print("Teste 3 - Adicionar Livro:")
print(b.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899, "Romance"))  # True
print(b.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899, "Romance"))  # LIVRO JÁ CADASTRADO!
print()

# Teste 4 - Emprestar Livro
print("Teste 4 - Emprestar Livro:")
print(b.emprestar_livros("Dom Casmurro", "12345678901", "1234"))  # True
print(b.emprestar_livros("Dom Casmurro", "12345678901", "1234"))  # Livro indisponível
print(b.emprestar_livros("Memórias Póstumas", "12345678901", "1234"))  # Livro não encontrado
print(b.emprestar_livros("Dom Casmurro", "00000000000", "1234"))  # CPF inválido
print()

# Teste 5 - Devolver Livro
print("Teste 5 - Devolver Livro:")
print(b.devolver_livros("Dom Casmurro", "12345678901", "1234"))  # True
print(b.devolver_livros("Dom Casmurro", "12345678901", "1234"))  # Usuário não tem empréstimo
print()

# Teste 6 - Histórico
print("Teste 6 - Histórico de Empréstimos:")
b.emprestar_livros("Dom Casmurro", "12345678901", "1234")
b.ver_historico("12345678901")  # deve mostrar histórico
print()

# Teste 7 - Exibir Usuários e Livros
print("Teste 7 - Listagem:")
b.exibir_usuarios()
b.exibir_livros()
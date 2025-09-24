class Usuario:
    _arquivo = "usuario.json"

    def __init__(self, nome, cpf, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__historico_livros = []
class Usuario:
    _arquivo = "usuario.json"

    def __init__(self, nome, cpf, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__historico_livros = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def senha(self):
        return self.__senha
    
    @property
    def historico_livros(self):
        self.__historico_livros
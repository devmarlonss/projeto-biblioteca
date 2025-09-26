class Usuario:
    def __init__(self, nome, cpf, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__livros_emprestados = []
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
    def livros_emprestados(self):
        return self.__livros_emprestados
    
    @property
    def historico_livros(self):
        return self.__historico_livros
    
    def usuario_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "senha": self.senha,
            "livros_emprestados": self.livros_emprestados,
            "historico_livros": self.historico_livros
        }
    
    @staticmethod
    def dict_usuario(usuario):
        """Método para transformar um dicionário em objeto"""
        return Usuario(usuario["nome"], usuario["cpf"], usuario["senha"], usuario["livros_emprestados"], usuario["historico_livros"])
    
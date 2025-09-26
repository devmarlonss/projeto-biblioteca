from datetime import date
from usuario import Usuario
from livro import Livro
from dados import Dados

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []

    def adicionar_usuario(self, nome, cpf, senha):
        if (self.verificar_cpf(cpf)):
            if (not self.buscar_usuario(cpf, show=False)):
                self.usuarios.append(Usuario(nome, cpf, senha))
                return True
            return "USUÁRIO JÁ CADASTRADO!"
        return "CPF INVÁLIDO!"

    def remover_usuario(self, cpf):
        for u in self.usuarios:
            if (u.cpf == cpf):
                self.usuarios.remove(u)
                return True
        return False

    def buscar_usuario(self, cpf, show=True, obj=False):
        for u in self.usuarios:
            if (u.cpf == cpf):
                if (obj):
                    return u
                if (show):
                    return (u.nome, u.cpf)
                return True
        return False

    def exibir_usuarios(self):
        if (self.usuarios):
            for p, u in enumerate(self.usuarios):
                print(f"{p+1} | Nome: {u.nome} | CPF: {u.cpf}")
        else:
            print("\n Nenhum usuário cadastrado!")

    def adicionar_livro(self, titulo, autor, ano, genero):
        if (not self.buscar_livro(titulo, show=False)):
            livro = Livro(titulo, ano, autor, genero)
            self.livros.append(livro)
            return True
        return "LIVRO JÁ CADASTRADO!"

    def remover_livro(self, titulo):
        for l in self.livros:
            if (l.titulo == titulo):
                self.livros.remove(l)
                return True
        return False

    def buscar_livro(self, titulo, show=True, obj=False):
        for l in self.livros:
            if (l.titulo == titulo):
                if (obj):
                    return l
                if (show):
                    return (l.titulo, l.autor, l.ano, l.genero, l.disponivel)
                return True
        return False
    
    def exibir_livros(self):
        if (self.livros):
            for p, l in enumerate(self.livros):
                print(f"{p+1} | Título: {l.titulo} | Autor: {l.autor} | Ano: {l.ano} | Gênero: {l.genero} | Disponível: {'Sim' if l.disponivel else 'Não'}")
        else:
            print("\n Nenhum livro cadastrado!")

    def emprestar_livros(self, titulo, cpf, senha):
        livro = self.buscar_livro(titulo, obj=True)
        if (livro):
            if livro.disponivel:
                if self.verificar_cpf(cpf):
                    usuario = self.buscar_usuario(cpf, obj=True)
                    if (usuario):
                        if self.verificar_senha(usuario, senha):
                            usuario.livros_emprestados.append(livro)
                            usuario.historico_livros.append([livro, date.today()])    
                            livro.disponivel = False
                            return True
                        return "Senha incorreta!"
                    return "Usuário não encontrado!"
                return  "CPF inválido!"
            return "Livro indisponível!"
        return "Livro não encontrado!"

    def devolver_livros(self, titulo, cpf, senha):
        livro = self.buscar_livro(titulo, obj=True)
        if (livro):
            if self.verificar_cpf(cpf):
                usuario = self.buscar_usuario(cpf, obj=True)
                if self.verificar_senha(usuario, senha):
                    if livro in usuario.livros_emprestados:
                        usuario.livros_emprestados.remove(livro)   
                        livro.disponivel = True
                        return True
                    return "Usuário não tem empréstimo do livro!"
                return "Senha Incorreta!"
            return  "CPF Inválido!"
        return "Livro não encontrado"
    
    def ver_emprestimos(self, cpf):
        if (self.verificar_cpf(cpf)):
            usuario = self.buscar_usuario(cpf, obj=True)
            if (usuario):
                print(f"USUÁRIO: {usuario.nome}")
                if (usuario.livros_emprestados):
                    for p, l in enumerate(usuario.livros_emprestados):
                        print(f"{p+1} - {l.titulo}")
                    return True
                return "Não há empréstimos!"
            return "Usuário não encontrado!"
        return "CPF Inválido!"
    
    def ver_historico(self, cpf):
        if (self.verificar_cpf(cpf)):
            usuario = self.buscar_usuario(cpf, obj=True)
            if (usuario):
                print(f"USUÁRIO: {usuario.nome}")
                if (usuario.historico_livros):
                    for p, l in enumerate(usuario.historico_livros):
                        print(f"{p+1} | Título: {l[0].titulo} | Data: {l[1]}")
                    return True
                return "Histórico vazio!"
            return "Usuário não encontrado!"
        return "CPF Inválido!"
    
    def carregar_usuarios(self):
        usuarios = Dados.carregar_dados("usuarios.json")
        for u in usuarios:
            usuario = Usuario(u["nome"], u["cpf"], u["senha"])

            livros_emprestados = []
            for l in u["livros_emprestados"]:
                livros_emprestados.append(Livro.dict_livro(l))
            usuario.livros_emprestados = livros_emprestados

            historico_livros = []
            for h in u["historico_livros"]:
                historico_livros.append(Livro.dict_livro(h[0]), h[1])
            usuario.historico_livros = historico_livros

            self.usuarios.append(usuario)

    def salvar_usuarios(self):
        dados = []
        for u in self.usuarios:
            livros_emprestados = []
            for l in u.livros_emprestados:
                livros_emprestados.append(l.livro_dict())

            historico_livros = []
            for h in u.historico_livros:
                historico_livros.append(h[0].livro_dict(), str(h[1]))

            dados.append({
                "nome": u.nome,
                "cpf": u.cpf,
                "senha": u.senha,
                "livros_emprestados": livros_emprestados,
                "historico_livros": historico_livros
            })
        Dados.salvar_dados("usuarios.json", dados)

    def carregar_livros(self):
        livros = Dados.carregar_dados("livros.json")
        for l in livros:
            self.livros.append(Livro.dict_livro(l))

    def salvar_livros(self):
        dados = []
        for l in self.livros:
            dados.append(Livro.livro_dict(l))
        Dados.salvar_dados("livros.json", dados)
    
    @staticmethod
    def verificar_senha(usuario, senha):
        """Método que retorna se é a senha do usuário"""
        return usuario.senha == senha
    
    @staticmethod
    def verificar_cpf(cpf):
        """Método que retorna se o CPF é válido"""
        return (cpf.isdigit() and len(cpf) == 11)
import json

class Dados:
    @staticmethod
    def salvar_dados(arquivo, dados):
        """Salva dados em arquivo JSON."""
        with open(arquivo, "w", encoding="utf-8") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)
    
    @staticmethod
    def carregar_dados(arquivo):
        """Carrega dados de um arquivo JSON, se existir."""
        with open(arquivo, "r", encoding="utf-8") as arq:
            return json.load(arquivo)

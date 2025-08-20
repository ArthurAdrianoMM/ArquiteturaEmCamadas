class Tarefa:
    def __init__(self, descricao: str):
        self.descricao = descricao.strip()  # tira espaços extras

    def __str__(self):
        return self.descricao

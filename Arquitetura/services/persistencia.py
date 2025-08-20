class PersistenciaArquivo:
    def __init__(self, nome_arquivo: str):
        self.nome_arquivo = nome_arquivo

    def salvar_em_arquivo(self, tarefa):
        with open(self.nome_arquivo, "a", encoding="utf-8") as f:
            f.write(str(tarefa) + "\n")

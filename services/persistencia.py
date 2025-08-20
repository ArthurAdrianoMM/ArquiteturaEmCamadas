class PersistenciaArquivo:
    def __init__(self, nome_arquivo: str):
        self.nome_arquivo = nome_arquivo

    def salvar_em_arquivo(self, tarefa):
        # O modo 'a' (append) adiciona ao final do arquivo
        with open(self.nome_arquivo, "a", encoding="utf-8") as f:
            f.write(str(tarefa) + "\n")

    # NOVO MÉTODO ADICIONADO AQUI
    def ler_do_arquivo(self):
        """Lê todas as tarefas do arquivo e retorna como uma lista."""
        try:
            with open(self.nome_arquivo, "r", encoding="utf-8") as f:
                # Usamos list comprehension para remover espaços em branco e quebras de linha
                tarefas = [linha.strip() for linha in f.readlines()]
                return tarefas
        except FileNotFoundError:
            # Se o arquivo ainda não existe, retorna uma lista vazia
            return []
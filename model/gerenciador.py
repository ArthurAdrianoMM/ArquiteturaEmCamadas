from services.persistencia import PersistenciaArquivo

class GerenciadorDeTarefas:
    def __init__(self):
        self.persistencia = PersistenciaArquivo("tarefas.txt")

    def adicionar_tarefa(self, tarefa):
        if not tarefa.descricao:  # validação simples
            return False
        try:
            self.persistencia.salvar_em_arquivo(tarefa)
            return True
        except Exception as e:
            print(f"Erro ao adicionar tarefa: {e}")
            return False

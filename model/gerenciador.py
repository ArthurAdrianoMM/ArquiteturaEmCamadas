from services.persistencia import PersistenciaArquivo

class GerenciadorDeTarefas:
    def __init__(self):
        self.persistencia = PersistenciaArquivo("tarefas.txt")

    def adicionar_tarefa(self, tarefa):
        if not tarefa.descricao:
            return False
        try:
            self.persistencia.salvar_em_arquivo(tarefa)
            return True
        except Exception as e:
            print(f"Erro ao adicionar tarefa: {e}")
            return False

    # NOVO MÉTODO ADICIONADO AQUI
    def listar_tarefas(self):
        """Solicita todas as tarefas ao serviço de persistência."""
        return self.persistencia.ler_do_arquivo()
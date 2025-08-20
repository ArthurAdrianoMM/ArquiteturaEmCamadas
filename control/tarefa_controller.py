from flask import Blueprint, render_template, request
from model.tarefa import Tarefa
from model.gerenciador import GerenciadorDeTarefas

tarefa_bp = Blueprint("tarefa", __name__)
gerenciador = GerenciadorDeTarefas()

# Rota principal (agora busca e exibe as tarefas)
@tarefa_bp.route("/", methods=["GET"])
def index():
    # Pede ao gerenciador a lista de tarefas
    lista_de_tarefas = gerenciador.listar_tarefas()
    # Envia a lista para o template
    return render_template("index.html", tarefas=lista_de_tarefas)

# Rota para adicionar tarefa (agora exibe a lista atualizada)
@tarefa_bp.route("/add_tarefa", methods=["POST"])
def add_tarefa():
    descricao = request.form.get("descricao")
    mensagem = ""
    
    if not descricao:
        mensagem = "⚠️ A descrição não pode ser vazia!"
    else:
        tarefa = Tarefa(descricao)
        sucesso = gerenciador.adicionar_tarefa(tarefa)
        if sucesso:
            mensagem = "✅ Tarefa adicionada com sucesso!"
        else:
            mensagem = "❌ Erro ao adicionar a tarefa."

    # Após a tentativa de adicionar, sempre busca a lista atualizada
    lista_de_tarefas = gerenciador.listar_tarefas()
    return render_template("index.html", mensagem=mensagem, tarefas=lista_de_tarefas)
from flask import Blueprint, render_template, request
from model.tarefa import Tarefa
from model.gerenciador import GerenciadorDeTarefas

# Criando um blueprint (para organizar as rotas do controlador)
tarefa_bp = Blueprint("tarefa", __name__)

# Instância do Gerenciador de Tarefas
gerenciador = GerenciadorDeTarefas()

# Rota principal (exibe o formulário)
@tarefa_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Rota para adicionar tarefa
@tarefa_bp.route("/add_tarefa", methods=["POST"])
def add_tarefa():
    descricao = request.form.get("descricao")

    if not descricao:
        return render_template("index.html", mensagem="⚠️ A descrição não pode ser vazia!")

    # Criar objeto Tarefa e adicionar via Model
    tarefa = Tarefa(descricao)
    sucesso = gerenciador.adicionar_tarefa(tarefa)

    if sucesso:
        return render_template("index.html", mensagem="✅ Tarefa adicionada com sucesso!")
    else:
        return render_template("index.html", mensagem="❌ Erro ao adicionar a tarefa.")

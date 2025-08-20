Atividade feita por arthur adriano, igor alves, joao maia

### Resumo do Fluxo Completo

#1.  **Execução**: Você vai rodar o comando `python app.py` no seu terminal.
#2.  **Inicialização**: O `app.py` cria a aplicação Flask e registra as rotas do `tarefa_controller.py`.
#3.  **Acesso do Usuário**: Ao acessar o endereço `http://127.0.0.1:5000/` no navegador, a rota `/` do controlador é acionada, renderizando o `view/index.html`.
#4.  **Adição de Tarefa**: O usuário preenche o formulário e clica em "Adicionar". O formulário envia os dados para a rota `/add_tarefa`.
#5.  **Processamento**: O controlador recebe a descrição, cria um objeto `Tarefa`, e o passa para o `GerenciadorDeTarefas`.
#.  **Persistência**: O gerenciador chama o serviço `PersistenciaArquivo`, que abre o `tarefas.txt` e salva a nova tarefa.
#.  **Feedback**: O controlador renderiza o `index.html` novamente, agora com uma mensagem de suce
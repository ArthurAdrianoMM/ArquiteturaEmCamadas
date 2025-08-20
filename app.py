from flask import Flask
from control.tarefa_controller import tarefa_bp

app = Flask(__name__, template_folder='view')

app.register_blueprint(tarefa_bp)

if __name__ == "__main__":
    app.run(debug=True)
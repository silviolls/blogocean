from flask import Flask, render_template

app = Flask("hello")
nomeAula = "Aula python para web"

@app.route("/usuario")
def usuario():
    usuario = [1, "Danilo Souza Miguel", "Professor"]
    alunos = ["Andre", "Lucas", "Maria", "Raiane"]
    return render_template("index.html", usuario=usuario, nome=nomeAula, aluno=alunos)

@app.route("/contatos")
def contato():
    return render_template("index.html", usuario=usuario, nome=nomeAula)
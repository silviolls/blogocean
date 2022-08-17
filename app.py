from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")
nomeAula = "Aula python para web"
posts = [
{
    "title":"Meu primeiro post",
    "body":"Este post eh o primeiro do blog",
    "autor":"Danilo Miguel",
    "created": datetime(2022,8,17)
},
{
    "title":"Meu segundo post",
    "body":"Este post eh o segundo do blog",
    "autor":"Danilo Miguel II",
    "created": datetime(2022,8,17)
},
{
    "title":"Meu terceiro post",
    "body":"Este post eh o terceiro do blog",
    "autor":"Danilo Miguel III",
    "created": datetime(2022,8,17)
}]


@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/usuario")
def usuario():
    usuario = [1, "Danilo Souza Miguel", "Professor"]
    alunos = ["Andre", "Lucas", "Maria", "Raiane"]
    return render_template("contatos.html", usuario=usuario, nome=nomeAula, aluno=alunos)

@app.route("/contatos")
def contato():
    return render_template("contatos.html", usuario=usuario, nome=nomeAula)

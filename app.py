from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    retorno = "<html><p>Hello <B>mundo</b></p></html>"
    return retorno

@app.route("/contatos")
def contato():
    return "Danilo de Souza, email danilo@souza"

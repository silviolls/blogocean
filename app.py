from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    retorno = "<html><p>Hello <B>mundo</b></p></html>"
    return retorno

@app.route("/contatos")
def contato():
    return """<html>
    <head>
       <title>Contatos</title>
    </head>
    <body>
       <h1>Danilo de Souza</h1>
       <h2>email danilo@souza.com.br</h2>
    </body>
    </html>"""

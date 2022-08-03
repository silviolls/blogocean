from flask import Flask

app = Flask("hello")

@app.route("/")

def hello():
    retorno = "<html><p>Hello <B>cambadinha da galera</b></p></html>"
    return retorno
from flask import Flask, render_template

app = Flask (__name__)


@app.route("/")
def inicial():
    return render_template("index.html")


@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


if __name__ == '__main__':
    app.run(debug=True)
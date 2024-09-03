from flask import Flask, render_template

app = Flask (__name__)


@app.route("/")
def incial():
    return render_template("index.html")


@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

if __name__ == '__main__':
    app.run(debug=True)
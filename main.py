from flask import Flask, redirect, url_for, render_template, request


app = Flask (__name__)
app.config['UPLOAD'] = '/upload'

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
    elif request.method == "POST":
        usuario = request.form.get("email")
        senha = request.form.get("senha")

        if usuario == "Ana Beatriz":
            if senha == "250323":
                return redirect(url_for('upload'))

        return render_template("login.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
       return render_template("upload.html")
    elif request.method == "POST":
        file = request.files["recipeFile"]
        caminho = app.config["UPLOAD_FOLDER"] + "/" + file.filename
        file.save(caminho)

        return render_template("cardapio.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'alguma_chave_secreta'  # Substitua por uma chave secreta mais segura


@app.route('/')
def home():
    return render_template('cardapio.html')


@app.route('/adicionar', methods=['POST'])
def adicionar_ao_carrinho():
    data = request.get_json()
    preco = data.get('preco')

    if 'total' not in session:
        session['total'] = 0

    session['total'] += preco
    return jsonify({'total': session['total']})


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
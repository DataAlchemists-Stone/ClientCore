from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/precomedio')
def precomedio():
    return render_template('precomedio.html')

@app.route('/lucroliquido')
def lucroliquido():
    return render_template('lucroliquido.html')

@app.route('/cac')
def cac():
    return render_template('cac.html')

@app.route('/artigos')
def artigos():
    return render_template('artigos.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(debug=True)

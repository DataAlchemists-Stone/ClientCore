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

if __name__ == '__main__':
    app.run(debug=True)

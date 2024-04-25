from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    decimal = int(request.form['decimal'])
    escolha = request.form['escolha']
    resultado = ""

    if escolha == "binario":
        resultado = decimal_to_binary(decimal)
    elif escolha == "octadecimal":
        resultado = decimal_to_octal(decimal)
    elif escolha == "hexadecimal":
        resultado = decimal_to_hexadecimal(decimal)

    return render_template('index.html', resultado=resultado)

@app.route('/', methods=['GET'])
def limpar():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
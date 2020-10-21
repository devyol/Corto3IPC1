from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/misDatos',methods=['GET'])
def misDatos():
    return jsonify({'carne':200512025,
                    'nombre': 'Erik Ronaldo Yol Patzan'})

@app.route('/binario-decimal/<binario>',methods=['POST'])
def binarioDecimal(binario):
    resultado = 0

    longitudCadena = len(binario)
    contador = 0
    while longitudCadena > 0:
        digito = 0
        if binario[contador] == '1':
            digito = 1

        resultado = resultado + (2**(longitudCadena-1))*digito
        longitudCadena -= 1
        contador += 1

    return jsonify({'resultado':resultado})



@app.route('/cifrarMensaje',methods=['POST'])
def cifrar():
    resultado = 'Sin Resultado'
    return jsonify({'resultado':resultado})


if __name__ == '__main__':
    app.run(debug=True)
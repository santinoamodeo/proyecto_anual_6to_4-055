from flask import Flask, render_template, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

bomba_encendida = False
hora_encendido = None
tiempo_total = timedelta()

@app.route('/')
def index():
    tiempo_ahora = tiempo_total
    if bomba_encendida and hora_encendido:
        tiempo_ahora += datetime.now() - hora_encendido
    return render_template('index.html', bomba_encendida=bomba_encendida, tiempo_bomba=str(tiempo_ahora))

@app.route('/bomba_on')
def bomba_on():
    global bomba_encendida, hora_encendido
    if not bomba_encendida:
        hora_encendido = datetime.now()
        bomba_encendida = True
    return redirect(url_for('index'))

@app.route('/bomba_off')
def bomba_off():
    global bomba_encendida, hora_encendido, tiempo_total
    if bomba_encendida and hora_encendido:
        tiempo_total += datetime.now() - hora_encendido
        hora_encendido = None
        bomba_encendida = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

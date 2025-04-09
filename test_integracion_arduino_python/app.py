from flask import Flask, render_template, redirect, url_for
from pyfirmata2 import Arduino, util
import time

app = Flask(__name__)

board = None
led_pin = None
rele_pin = None
rele2_pin = None

led_encendido_inicio = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encender")
def encender():
    global led_encendido_inicio
    if led_pin:
        led_pin.write(1)
        led_encendido_inicio = time.time()
    return redirect(url_for("index"))

@app.route("/apagar")
def apagar():
    if led_pin:
        led_pin.write(0)
        if led_encendido_inicio:
            duracion = round(time.time() - led_encendido_inicio, 2)
            print(f"💡 El LED estuvo encendido durante {duracion} segundos")
    return redirect(url_for("index"))

@app.route("/rele_on")
def rele_on():
    if rele_pin:
        rele_pin.write(1)
    return redirect(url_for("index"))

@app.route("/rele_off")
def rele_off():
    if rele_pin:
        rele_pin.write(0)
    return redirect(url_for("index"))

@app.route("/rele2_on")
def rele2_on():
    if rele2_pin:
        rele2_pin.write(1)
    return redirect(url_for("index"))

@app.route("/rele2_off")
def rele2_off():
    if rele2_pin:
        rele2_pin.write(0)
    return redirect(url_for("index"))

if __name__ == "__main__":
    try:
        board = Arduino('COM5')  # Asegurate que sea el puerto correcto
        led_pin = board.get_pin('d:13:o')
        rele_pin = board.get_pin('d:8:o')     # Rele 1 en pin 8
        rele2_pin = board.get_pin('d:9:o')    # Rele 2 en pin 9
        print("✅ Arduino conectado correctamente")
    except Exception as e:
        print(f"⚠️ No se pudo conectar al Arduino: {e}")
        board = None
        led_pin = None
        rele_pin = None
        rele2_pin = None

    app.run(debug=False)

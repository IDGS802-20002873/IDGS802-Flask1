from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/cinepolis", methods=["GET"])
def cinepolis():
    return render_template("cinepolis.html")

def descuentoTarjeta(tarjeta, costo):
    if tarjeta == "1":
        descuentoT = costo * 0.1
        costo = costo - descuentoT
        return costo
    else:
        return costo

def descuentoBoletos(cantidadBol, costo, tarjeta):
    if cantidadBol > 7:
        costo = "La cantidad de boletos sobrepasa el limite por persona"
        return costo
    elif cantidadBol > 5 & cantidadBol <= 7:
        costo = descuentoTarjeta(tarjeta, costo)
        descuento = costo * 0.15
        costo = costo - descuento
        return costo
    elif cantidadBol >= 3 & cantidadBol <= 5:
        costo = descuentoTarjeta(tarjeta, costo)
        descuento = costo * 0.15
        costo = costo - descuento
        return costo
    else:
        costo = descuentoTarjeta(tarjeta, costo)
        return costo

@app.route("/resultado", methods=["POST"])
def resultado():
    nombre = request.form.get("txtNombre")
    cantidadCom = int(request.form.get("txtCantidadCom"))
    cantidadBol = int(request.form.get("txtCantidadBol"))
    tarjeta = request.form.get("btnTarjeta")
    costoBol = int(12)
    costo = cantidadCom * costoBol
    total = descuentoBoletos(cantidadBol, costo, tarjeta)
    res = "<h1>¡Hola {}! la cantidad a pagar es = {}</h1>".format(nombre, total)
    return render_template("resultadoCine.html",res=res)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
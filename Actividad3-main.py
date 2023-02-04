from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/cinepolis", methods=["GET"])
def cinepolis():
    return render_template("cinepolis.html")

def descuentoTarjeta(tarjeta, costo):
    if tarjeta == "1":
        descuentoT = costo * 0.10
        return descuentoT
    else:
        return 0

def descuentoBoletos(cantidadBol, costo, tarjeta):
    if cantidadBol > 7:
        total = "La cantidad de boletos sobrepasa el limite por persona"
        return total
    elif cantidadBol > 5 & cantidadBol <= 7:
        descuento = costo * 0.15
        descuentoT = descuentoTarjeta(tarjeta, costo)
        total = (costo - descuento) - descuentoT
        return round(total,2)
    elif cantidadBol >= 3 & cantidadBol <= 5:
        descuentoT = descuentoTarjeta(tarjeta, costo)
        descuento = costo * 0.10
        total = (costo - descuento) - descuentoT
        return round(total,2)
    else:
        descuentoT = descuentoTarjeta(tarjeta, costo)
        total = costo - descuentoT
        return round(total,2)

@app.route("/resultado", methods=["POST"])
def resultado():
    nombre = request.form.get("txtNombre")
    cantidadCom = int(request.form.get("txtCantidadCom"))
    cantidadBol = int(request.form.get("txtCantidadBol"))
    tarjeta = request.form.get("btnTarjeta")
    costoBol = int(12)
    costo = (cantidadBol * cantidadCom) * costoBol
    print(costo)
    total = descuentoBoletos(cantidadBol, costo, tarjeta)
    print(descuentoBoletos(cantidadBol, costo, tarjeta))
    res = "¡Hola {}! la cantidad a pagar es = {}".format(nombre, total)
    return render_template("resultadoCine.html",res=res)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
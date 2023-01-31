from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route("/operasBas", methods=["GET"])
def operasBas():
    return render_template("operasBas.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    n1=request.form.get("txtNum1")
    n2=request.form.get("txtNum2")
    numSum=request.form.get("txtNum1")
    texto = n1
    while int(n2)!=1:
        n1 = int(n1)+int(numSum) 
        n2 = int(n2)-1
        texto += " + " + str(numSum)

    res = str(texto) + " = " + str(n1)
    return render_template("resultado.html",res=res)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
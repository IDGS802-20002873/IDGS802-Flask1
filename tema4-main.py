'''
Estructura base para trabajar con Python
'''

from flask import Flask
#Libreria para hacer peticiones
from flask import request
app=Flask(__name__)

@app.route("/operasBas",methods=["GET", "POST"])
def operasBas():

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        return "<h2> La suma es: {} </h2>".format(str(int(num1)+int(num2)))
    else:
        return '''
        <form action="/operasBas" method = "POST">
            <label>N1: </label>
            <input type="text" name="num1" /><br></br>
            <label>N2: </label>
            <input type="text" name="num2" /><br></br>
            <input type="radio" name"suma" /><br></br>
            <input type="radio" name"resta" /><br></br>
            <input type="radio" name"multiplicacion" /><br></br>
            <input type="radio" name"division" /><br></br>
            <input type="submit" value="calcular"/>
        </form>
        '''


if __name__ == "__main__":
    app.run(debug=True, port=3000)
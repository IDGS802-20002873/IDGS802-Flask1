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
        i = request.form.get("i")
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        if str(i) == "1":
            return "<h2> La suma es: {} </h2>".format(str(int(num1)+int(num2)))
        elif str(i) == "2":
            return "<h2> La resta es: {} </h2>".format(str(int(num1)-int(num2)))   
        elif str(i) == "3":
            return "<h2> La multiplicación es: {} </h2>".format(str(int(num1)*int(num2)))   
        elif str(i) == "4":
            return "<h2> La división es: {} </h2>".format(str(int(num1)/int(num2)))   
    else:
        return '''
        <form action="/operasBas" method = "POST">
            <label>N1: </label>
            <input type="text" name="num1" /><br></br>
            <label>N2: </label>
            <input type="text" name="num2" /><br></br>
            <div>
            <input type="radio" name="i" value="1">
            <label for="i">Sumar</label>
            </div>
            <div>
            <input type="radio" name="i" value="2">
            <label for="i">Restar</label>
            </div>
            <div>
            <input type="radio" name="i" value="3">
            <label for="i">Multiplicar</label>
            </div>
            <div>
            <input type="radio" name="i" value="4">
            <label for="i">Dividir</label>
            </div><br></br>
            <input type="submit" value="calcular"/>
        </form>
        '''


if __name__ == "__main__":
    app.run(debug=True, port=3000)
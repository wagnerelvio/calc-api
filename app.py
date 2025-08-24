from flask import Flask, request

app = Flask(__name__)

@app.route("/calc", methods=["GET"])
def calc():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        op = request.args.get("op", "soma")

        if op == "soma":
            resultado = a + b
        elif op == "sub":
            resultado = a - b
        elif op == "mult":
            resultado = a * b
        elif op == "div":
            if b == 0:
                return {"erro": "Divisão por zero não permitida"}, 400
            resultado = a / b
        else:
            return {"erro": "Operação inválida. Use soma, sub, mult ou div"}, 400

        return {
            "a": a,
            "b": b,
            "operacao": op,
            "resultado": resultado
        }
    except Exception as e:
        return {"erro": str(e)}, 400

if __name__ == "__main__":
    app.run(debug=True)

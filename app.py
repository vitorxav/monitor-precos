from flask import Flask, render_template, request, jsonify
from scraper.selenium_scraper import get_price_with_selenium
from alert import enviar_alerta

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/verificar", methods=["POST"])
def verificar():
    data = request.json
    url = data.get("url")
    selector = data.get("selector")
    preco_desejado = float(data.get("preco_desejado"))
    email = data.get("email")

    preco_atual = get_price_with_selenium(url, selector)

    if preco_atual is not None:
        if preco_atual <= preco_desejado:
            mensagem = f"✅ Preço encontrado: R$ {preco_atual:.2f} (abaixo de R$ {preco_desejado:.2f})"
            enviar_alerta(email, preco_atual, url)
        else:
            mensagem = f"📈 Preço atual: R$ {preco_atual:.2f} (acima do desejado)"
    else:
        mensagem = "❌ Não foi possível obter o preço."

    return jsonify({
        "mensagem": mensagem,
        "preco": preco_atual
    })

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from scraper.selenium_scraper import get_price_with_selenium
from alert import enviar_alerta
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    preco_atual = None
    mensagem = ""

    if request.method == "POST":
        url = request.form.get("url")
        selector = request.form.get("selector")
        preco_desejado = request.form.get("preco_desejado")
        email = request.form.get("email")

        # Validação de campos
        if not is_valid_url(url):
            mensagem = "❌ URL inválida."
            return render_template("index.html", mensagem=mensagem)

        try:
            preco_desejado = float(preco_desejado)
        except ValueError:
            mensagem = "❌ Preço desejado inválido."
            return render_template("index.html", mensagem=mensagem)

        print(f"[INFO] Verificando: {url} com seletor: {selector}")
        preco_atual = get_price_with_selenium(url, selector)
        print(f"[INFO] Preço atual: {preco_atual} | Desejado: {preco_desejado}")

        if preco_atual is not None:
            if preco_atual <= preco_desejado:
                mensagem = f"✅ Preço encontrado: R$ {preco_atual:.2f} (abaixo de R$ {preco_desejado:.2f})"
                assunto = "🔔 Alerta de Preço: Oferta Encontrada!"
                corpo = f"O produto que você está monitorando está com preço de R$ {preco_atual:.2f}.\n\nLink: {url}"
                enviar_alerta(email, preco_atual, url)
                print(f"[EMAIL] Enviado para {email}")
            else:
                mensagem = f"📈 Preço atual: R$ {preco_atual:.2f} (acima do desejado)"
        else:
            mensagem = "❌ Não foi possível obter o preço."

    return render_template("index.html", mensagem=mensagem, preco=preco_atual)

if __name__ == "__main__":
    app.run(debug=True)

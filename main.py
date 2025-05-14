from scraper.selenium_scraper import get_price_with_selenium
from alert import enviar_alerta
import time

# === CONFIGURAÇÕES ===
URL_PRODUTO = "https://www.kabum.com.br/produto/205760/gravador-dvd-rw-sata-asus-24x-drw-24f1mt-blk-b-as"
CSS_SELECTOR = "#blocoValores > div.sc-a24aba34-3.hSVqxN > div.sc-a24aba34-1.cpLDBn > div > h4"
PRECO_DESEJADO = 90.00
INTERVALO_CHECAGEM = 1800  # 30 minutos (em segundos)

def monitorar():
    while True:
        print(f"\n🔍 Verificando preço do produto: {URL_PRODUTO}")
        preco = get_price_with_selenium(URL_PRODUTO, CSS_SELECTOR)

        if preco is None:
            print("[ERRO] Não foi possível obter o preço.")
        elif preco <= PRECO_DESEJADO:
            print(f"✅ Preço encontrado: R$ {preco:.2f} — abaixo do desejado!")
            enviar_alerta(preco, URL_PRODUTO)
        else:
            print(f"[INFO] Preço atual: R$ {preco:.2f} — acima do alvo de R$ {PRECO_DESEJADO:.2f}")

        print(f"Aguardando {INTERVALO_CHECAGEM} segundos para nova verificação...\n")
        time.sleep(INTERVALO_CHECAGEM)

if __name__ == "__main__":
    monitorar()

import time
from scraper.selenium_scraper import get_price_with_selenium
from alert import enviar_alerta

def monitorar_produto(url, css_selector, preco_alvo, intervalo=60):
    while True:
        print("[INFO] Verificando preço...")

        preco_atual = get_price_with_selenium(url, css_selector)

        if preco_atual is None:
            print("[ERRO] Preço não encontrado.")
        else:
            print(f"[INFO] Preço atual: R$ {preco_atual:.2f}")

            if preco_atual <= preco_alvo:
                print("[ALERTA] O preço está ABAIXO do alvo!")
                enviar_alerta(preco_atual, url)
            else:
                print("O preço está ACIMA do alvo!")

        print(f"[INFO] Aguardando {intervalo} segundos para nova verificação...\n")
        time.sleep(intervalo)
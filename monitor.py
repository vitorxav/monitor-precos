import time
from scraper.selenium_scraper import get_price_with_selenium
# from alert import enviar_alerta

def monitorar_produto(url, css_selector, preco_alvo, intervalo=60):
    """
    Monitora o preço de um produto e avisa quando estiver abaixo do valor desejado.

    url: link do produto
    css_selector: seletor CSS do preço
    preco_alvo: valor desejado (alvo)
    intervalo: tempo (em segundos) entre cada checagem
    """
    while True:
        print("[INFO] Verificando preço...")

        preco_atual = get_price_with_selenium(url, css_selector)

        if preco_atual is None:
            print("[ERRO] Preço não encontrado.")
        else:
            print(f"[INFO] Preço atual: R$ {preco_atual:.2f}")

            if preco_atual <= preco_alvo:
                print("[ALERTA] O preço está ABAIXO do alvo!")
            #    enviar_alerta(preco_atual, url)
            else:
                print("O preço está ACIMA do alvo!")

        print(f"[INFO] Aguardando {intervalo} segundos para nova verificação...\n")
        time.sleep(intervalo)

#if __name__ == "__main__":
#    url = "https://www.kabum.com.br/produto/205760/gravador-dvd-rw-sata-asus-24x-drw-24f1mt-blk-b-as"  # Substitua com seu link
#    css_selector = "#blocoValores > div.sc-a24aba34-3.hSVqxN > div.sc-a24aba34-1.cpLDBn > div > h4"                # Substitua com seu seletor
#    preco_alvo = 90.00                                # Alvo em R$

#    monitorar_produto(url, css_selector, preco_alvo, intervalo=120)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def get_price_with_selenium(url, css_selector):
    # Configurações para rodar o Chrome em modo invisível (sem abrir janela)
    options = Options()
    options.add_argument("--headless")  # Roda em segundo plano
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Instancia o driver do Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)  # Acessa a página
        time.sleep(3)  # Espera a página carregar (pode ajustar o tempo)

        # Encontra o elemento do preço usando seletor CSS
        price_element = driver.find_element(By.CSS_SELECTOR, css_selector)

        # Limpa o texto (R$, pontos, vírgulas etc.)
        price_text = price_element.text.strip().replace('R$', '').replace('.', '').replace(',', '.')
        return float(price_text)

    except Exception as e:
        print(f"[ERRO] Não foi possível obter o preço: {e}")
        return None

    finally:
        driver.quit()  # Fecha o navegador (mesmo em segundo plano)


#if __name__ == "__main__":
    # Link de exemplo (Notebook Dell na Kabum)
#    url = "https://www.kabum.com.br/produto/205760/gravador-dvd-rw-sata-asus-24x-drw-24f1mt-blk-b-as"

    # Seletor CSS do preço (copiado com o botão direito > Inspecionar > Copy selector)
#    css_selector = "#blocoValores > div.sc-a24aba34-3.hSVqxN > div.sc-a24aba34-1.cpLDBn > div > h4"

    # Chama a função para buscar o preço
#    preco = get_price_with_selenium(url, css_selector)

#    if preco is not None:
#        print(f"Preço encontrado: R$ {preco:.2f}")
#    else:
#        print("Não foi possível encontrar o preço.")

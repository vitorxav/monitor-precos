from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def get_price_with_selenium(url, css_selector):
    # Configurações para rodar o Chrome sem abrir janela
    options = Options()
    options.add_argument("--headless")  # Roda em segundo plano
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        time.sleep(3)

        price_element = driver.find_element(By.CSS_SELECTOR, css_selector)

        # Limpa o texto
        price_text = price_element.text.strip().replace('R$', '').replace('.', '').replace(',', '.')
        return float(price_text)

    except Exception as e:
        print(f"[ERRO] Não foi possível obter o preço: {e}")
        return None

    finally:
        driver.quit()
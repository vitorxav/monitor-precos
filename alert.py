import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CONFIGURAÇÕES
EMAIL_REMETENTE = "vitordias.xavier1@gmail.com"
SENHA_APP = "xqyf qikz hhpw plcg"
EMAIL_DESTINATARIO = "vitoremanuezinho@gmail.com"


def enviar_alerta(preco, url):

    assunto = "📢 Alerta de Preço: Produto abaixo do valor desejado!"
    corpo = f"""
    O produto que você está monitorando está com preço baixo!

    💰 Novo preço: R$ {preco:.2f}
    🔗 Link do produto: {url}

    Verifique agora!
    """

    # Montar e-mail
    mensagem = MIMEMultipart()
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = EMAIL_DESTINATARIO
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_REMETENTE, SENHA_APP)
            servidor.send_message(mensagem)
            print("[EMAIL] Alerta enviado com sucesso!")
    except Exception as e:
        print(f"[ERRO] Falha ao enviar o alerta por e-mail: {e}")


#if __name__ == "__main__":
#    enviar_alerta(2599.90, "https://www.kabum.com.br/produto/123456")

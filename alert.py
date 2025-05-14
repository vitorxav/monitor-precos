import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CONFIGURAÇÕES
EMAIL_REMETENTE = "vitordias.xavier1@gmail.com"
SENHA_APP = "xqyf qikz hhpw plcg"

def enviar_alerta(email_destinatario, preco, url):
    assunto = "📢 Alerta de Preço: Produto abaixo do valor desejado!"
    corpo = f"""
    O produto que você está monitorando está com preço baixo!

    💰 Novo preço: R$ {preco:.2f}
    🔗 Link do produto: {url}

    Verifique agora!
    """

    mensagem = MIMEMultipart()
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = email_destinatario
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

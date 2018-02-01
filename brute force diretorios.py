import requests

url = "http://www.vivaolinux.com.br/"
arquivo = open("/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt")
linhas = arquivo.readlines()


for linha in linhas:
    if requests.get(url+linha) == 200:
        resposta = requests.get(url+linha)
    
        print "\n",url+linha
        print resposta.status_code
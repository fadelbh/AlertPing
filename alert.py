__author__ = 'Humberto'

#!/usr/bin/env
# -*- coding: utf-8 -*-

import os, re

print
#Tupla de IP's
ipall = [("FNT-ESCCA-AR-A01", "173.194.42.1"), ("FNT-ESCCA-AR-A02", "173.194.42.2"), ("FNT-ESCCA-AR-A03", "173.194.42.3"),
       ("FNT-ESCCA-AR-A04",	"173.194.42.4"), ("FNT-ESCCA-AR-A05", "173.194.42.5"), ("FNT-ESCCA-AR-A06", "173.194.42.6"),
       ("FNT-ESCCA-AR-A07",	"173.194.42.7"), ("FNT-ESCCA-AR-A08", "173.194.42.8"), ("FNT-ESCCA-AR-A09", "173.194.42.9"),
       ("FNT-ESCCA-AR-A10",	"173.194.42.10"), ("FNT-ESCCA-AR-A11", "173.194.42.11"), ("FNT-ESCCA-AR-A12", "173.194.42.12"),
       ("FNT-ESCCA-AR-A13",	"173.194.42.13"), ("FNT-ESCCA-AR-A14", "173.194.42.14"), ("FNT-ESCCA-AR-A15", "173.194.42.15"),
       ("FNT-ESCCA-AR-A16",	"173.194.42.16"), ("FNT-ESCCA-AR-A17", "173.194.42.17"), ("FNT-ESCCA-AR-A18", "173.194.42.18"),
       ("FNT-ESCCA-AR-A19",	"173.194.42.19"), ("FNT-ESCCA-AR-A20", "173.194.42.20"), ("FNT-ESCCA-AR-A21", "173.194.42.21"),
       ("FNT-ESCCA-AR-A22",	"173.194.42.22"), ("FNT-ESCCA-AR-A23", "173.194.42.23"), ("FNT-ESCCA-IN-I01", "173.194.42.24")]

ipall.sort() #Ordenando a Tupla

#Bloco para escolha do passo a ser executado
#----------------------------------------------------------------------------------
print "Selecione a opcao abaixo \n" \
      "1 - Verificar os IP's da lista \n" \
      "2 - Executar o teste de ping na lista"
check = raw_input("Selecione (1 ou 2):\n"
                  "")
while check != "1" and check != "2":
    print "Opcao invalida"
    check = raw_input("Selecione (1 - Verificar lista atual | 2 - Executar o teste de ping na lista):\n")
if check == "1":
    print
    print "+" * 62
    print "Ip's a serem verificados."
    print "+" * 62
    print
    for ip2 in ipall:
        print "Elemento: %s" %ip2[0]
    print
else:
    pass
#Bloco que executa a verificacao de resposta dos IP's
#----------------------------------------------------------------------------------
    print "=" * 62
    print "              Verificando resposta dos IP's..."
    print "=" * 62
    print "-" * 62
    print "     Elemento      |     Ip Fonte     |        Status        |"
    print "-" * 62
    for ip in ipall:
        cmd = "ping -c2 " + ip[1]
        r = "".join(os.popen(cmd).readlines()) #Executa o comando de ping e captura a linha de resposta
        if re.search ("64 bytes from", r): #Faz analise da linha capturada anteriormente e informa o status da conexao
            print "-" * 62
            print "%18s | %14s   |      Conexao OK      |" %(ip[0], ip[1])
        else:
            print "-" * 62
            print "%18s | %14s   |    Falha na Conexao  |" %(ip[0], ip[1])
print "-" * 62
print

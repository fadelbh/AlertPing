__author__ = 'Humberto'

#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from operator import itemgetter
import os, re

#Funcao de validacao dos dados
def verificar(x):
    while x == '':
       	print 'Esse campo e obrigatorio!'
       	x = input('Digite novamente: \n')
    return x

#Cadastro de novos Elementos e IP's
#----------------------------------------------------------------------------------
ips = {}
v = "s"
while v == "s":
    print "Cadastro de Novos Elementos!"
    print
    v = raw_input("Voce deseja cadastrar novos elementos (S/N)? ")
    print
    if v == "s" or v == "S":
        element = raw_input("Informe o Elemento: ")
        i = raw_input("Informe o IP: ")
        ips[i] = element
    elif v == "n" or v == "N":
        print "Cadastro OK!"
        break
    else:
        print "Opcao invalida!"

#Organizando o dicionario de acordo com os values
#----------------------------------------------------------------------------------
ips2 = sorted(ips.items(), key=itemgetter(1))
#Bloco informativo de quais IP's serao verificados
#----------------------------------------------------------------------------------
print
print "+" * 62
print "Ip's a serem verificados."
print "+" * 62
print
for ip2 in ips2:
    print "Elemento: %18s - IP: %s" %(ip2[1], ip2[0])
print

#Bloco que executa a verificacao de resposta dos IP's
#----------------------------------------------------------------------------------
print "Verificando conexao dos IP's..."
print
print "-" * 62
print "     Elemento      |     Ip Fonte     |        Status        |"
print "-" * 62
for ip in ips.keys():
    cmd = "ping -c3 " + ip
    r = "".join(os.popen(cmd).readlines()) #Executa o comando de ping e captura a linha de resposta
    if re.search ("64 bytes from", r): #Faz analise da linha capturada anteriormente e informa o status da conexao
        print "-" * 62
        print "%18s | %16s |    Conexao OK        |" %(ips[ip], ip)
    else:
        print "-" * 62
        print "%18s | %16s |    Falha na Conexao  |" %(ips[ip], ip)
print "-" * 62
print
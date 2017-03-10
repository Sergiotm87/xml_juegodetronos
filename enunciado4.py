# -*- coding: utf-8 -*-
from lxml import etree
#
#Introduce el nombre de un rey y muestra el tamaño de su ejercito en la mayor batalla en la que haya participado
#
doc = etree.parse('batallasjuegotronos.xml')
raiz=doc.getroot()

#rey=raw_input("introduce el nombre de un rey")
#ej. Robb Stark,Stannis Baratheon
rey="Robb Stark"

#he eliminado el caracter 'ñ' del xml porque xpath no aceptaba ese caracter a pesar de que ambos ficheros estan codificados con utf-8

rutarey="//rey_atacante/text()|//rey_defensor/text()"

#ejercito="//ejercito_atacante[rey_atacante/text()='"+rey+"']/@ejercito"

ejercito="//ejercito_atacante[rey_atacante/text()='"+rey+"']/@ejercito| //ejercito_defensor[rey_defensor/text()='"+rey+"']/@ejercito"


reyes=raiz.xpath(rutarey)
if rey in reyes:
    ejercitos=raiz.xpath(ejercito)

print ejercitos

#pasamos la lista de strings a una lista de numeros pero al mapear la lista como integer da una excepcion ValueError debido que no puede
#pasar a numero un valor como ' ' asi que usamos lo siguiente, la lista sin repetir y una estructura con la misma funcion que map(int,list)


x = list(set(ejercitos))

mayorejercito=0

for elem in x:
   if elem.strip():
       n = int(elem)
       if n>mayorejercito:
           mayorejercito=n

print mayorejercito

#ruta ejercito contrincante con el mismo nodo padre:

ejenemigo="//contendientes/ejercito_atacante[@ejercito="+str(mayorejercito)+"][//rey_atacante/text()='"+rey+"']/following-sibling::ejercito_defensor"
enemigo=raiz.xpath(ejenemigo)

ejercitoenemigo= enemigo[0].get('ejercito')

print ejercitoenemigo


#falta mostrar el nombre de dicha batalla

#print "la mayor batalla de",rey,"fue",nombrebatalla,"en la que participaron",mayorejercito+ejercitoenemigo
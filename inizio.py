#inizio corso di python
print('hello world')
#variabile stringa
stringa = 'stringa'
print(stringa)
print(type(stringa))
#trasformare un integer in una stringa
numero = 5
print(type(numero))
numero_stringa = str(numero)
print(numero_stringa)
print(type(numero_stringa))
#operatore modulo: restituisce il resto di una divisione
4%2
#concatenare stringa e numero
a= 'il risultato è '
b= 3
c = a + str(b)
print(c)
#nelle operazioni ri rispettano le regole matematiche (si fannno prima le operazioni tra parentesi ad esempio)
#per commentare lunghe senzioni 
''' posso dire tante cose
tanto non le legge'''

#per tutte le operazioni matematiche
import math
#le funzioni
#quando creo un afunzione a è il parametro
def stampa_val (a):
  print(a)
#a è valido solo all'interno della funzione, solo finchè è indentato. è una variabile locale
#infatti posso assegnare anche un altro valore con lo stesso nome a
a = 8
#questo a è un parametro globale
#quando richiamo la funzione tra le parentesi c'è l'argomento
stampa_val(89)
stampa_val(a) #in questo caso mi prende come argomento la variabile globale a

#funzione per calcolare l'area di un rettangolo
def area_rett (b,h):
    area = b*h
    print(area)
area_rett(5,4)

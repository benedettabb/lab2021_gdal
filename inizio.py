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

#sintassi condizionale
a = 0.5
#se a è maggiore di 2 
if a> 2:
  print ('maggiore')
#altrimenti...
else:
  print('minore')
  
#funzione per stabilire se un numero è pari o dispari
def num_pari (n):
  #se il risultato della divisione per 2 da resto 0... (== uguaglianza; = assegnazione)
  if n%2==0:
    print ('Il numero' + str(n) + 'è pari')
  else:
    print ('il numero' +str(n) + 'è dispari')
 
num_pari(8)

#operatori
#MAGGIORE >
#MINORE <
#UGUALE ==
#MAGGIORE UGUALE >=
#DIVERSO !=

#operatori booleani, AND OR NOT
#funzione che mi dice se il numero che inserisco è compreso tra due valori
def zeroDieci (n):
  if n>=0 and n<=10:
    print ('Il numero ' +str(n)+ ' è compreso tra 0 e 10')
  else:
    print ('Il numero ' +str(n)+ ' non è compreso tra 0 e 10')
    
zeroDieci(6)
zeroDieci(11)
zeroDieci(10)


#funzione che mi dice se un numero è maggiore di un altro 
def maggiore (n, m):
    if n > m:
        return ('Il numero ' + str(n) + ' è maggiore di ' + str(m))
    elif n==0:
        return ('Il numero ' + str(m) + ' è uguale a ' + str(n))
    else:
        return ('Il numero ' + str(m) + ' è maggiore di ' + str(n))
print(maggiore(8,6))


#---CONTO ALLA ROVESCIA con funzione dentro la funzione
def contoRovescia (a):
    #se a è uguale a zero stampa la stringa
    if a ==0:
        print('Il conto alla rovescia è finito')
    #se a è diverso da 0 stampa a e poi richiama la funzione con a-1
    else:
        print(a)
        contoRovescia (a-1)
        #richiamo una funzione all'interno della funzione. poi a-1 diviene
        #il nuovo argomento della funzione
        
contoRovescia(10)

#---CONTO ALLA ROVESCIA con WHILE
def cicloWhile (a):
    #finché a è maggiore di 0
    while a>0:
        print(a)
        a =a-1
    print('Il conto alla rovescia è finito')
    #finchè n non è più maggiore di 0 --> il ciclo while si interrompe


#CICLO INFINITO ---> i loop infiniti si bloccano con Ctrl+C
def cicloInfinito (a):
    while a>0:
        print(a)
        a =a+1
    print('Il conto alla rovescia è finito')
cicloInfinito (3)


#listaaa
a = [5,3,2,1,3,4,4,9]
print(a)
#lista di listee
b = [4,3,1,['d',2,3,'q','p'],a]
print(b)
  

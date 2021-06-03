import math
#funzione da celsius a fahrenheit
def c_f (c):
  f = (9*c + (32*5))/5
  print (str(c) + 'gradi Celsius equivalgono a ' + str(f) + 'gradi Fahrenheit')
 
c_f(20)

#funzione che prende come parametri le coordinate cartesiane di x e di y e calcola la distanza tra i due punti
def distanza (ax, ay, bx, by):
  distanza = math.sqrt ((ax-bx)^2)+((ay-by)^2)
  print ('la distanza tra i due punti è:' +str(distanza))

distanza (8,2,6,4)

#i primi elementi di due liste sono uguali?
lista1 (8, 5, 4, 2, 5)
lista2 (8, 3, 2, 5, 8)

def eguals (l1,l2):
  if l1[0] == l2[0]:
    print ('I primi due elementi delle liste sono uguali')
   else:
    print('I primi due elementi delle liste NON sono uguali')
    
eguals (lista1, lista2)


#qual'è il numero maggiore in una lista?
def max_in_lista (l):
  m=0
  for num in l:
    if num > m:
      m = num
    else:
      pass

 

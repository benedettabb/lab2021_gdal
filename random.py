import random
#numero casuale da 0 a 1
a = int (random.random()*100) #se moltiplico per 100 e metto int ho un numero pseudo-casuale intero da 0 a 100
print(a)

#creo una lista di 20 numeri consecutivi
a=range(20)
print (list(a))

#funzione per sapere se il numero in input è presente in una lista di numeri causali
def guess_n (n):
  #creo una lista vuota
  lista =[]
  for num in range (10):
    #funzione che genera un numero intero compreso tra 1 e 100
    b = random.randint(1, 100)
    lista.append(b) #aggiungo il numero alla lista
  print(lista) #printo la lista di numeri casuali
  if n in lista:
    print (str(n) +' è presente nella lista')
  else:
    print (str(n) +' NON è presente nella lista')
      
     
  

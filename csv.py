import csv
#carico il dataset
dataset = open("C:/Users/UTENTE/Desktop/UNIBO/GEOGRAFIA/II ANNO/LAB/python/montecristo_point.csv")
#apro la tabella
table = csv.reader (dataset, delimiter = ',') #ogni riga è una lista. quindi posso prendere ogni elemento con gli indici[]
#table = csv.DictReader (dataset, delimiter =',') #aggiunge anche l'header ad ogni riga -- per chiamare gli elementi nelle righe non posso usare gli indici ma il nome che sta nell'header

#printo ogni riga nella tabella
for row in table:
  print (row) 
  #print (row['coordy'])
  
#creo una lista per l'header
header = ['id', 'coordx', 'coordy', 'h')
#creo una lista contenente tutte le altre righe del file. devo prima creare una lista vuota
l = []
for row in table:  #per ogni riga della mia tabella
  l.append(row) #aggiungi la riga alla mia lista vuota
print(l) #ho la mia lista di liste
          
#creo un nuovo file csv  -- cambio il nome ma stessa directory!        
out_table = open("C:/Users/UTENTE/Desktop/UNIBO/GEOGRAFIA/II ANNO/LAB/python/montecristo_point_header.csv")
new_tab = csv.writer (out_table, delimiter = ',') #creo una nuova tabella 
#aggiungo l'header
new_table.writerow(header) #il comando è writerow, della libreria csv
#aggiungo la lista di liste
new_table.writerows(l) #al plurale: writerows
          
#devo sempre chiudere tutto dopo
dataset.close()
out_table.close()
          


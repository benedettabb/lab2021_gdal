import csv
import pandas as pd
#carico il dataset
my_csv= open("/home/benedetta/Scrivania/UNIBO/LAB/montecristo_point.csv")
#apro la tabella
tabella = csv.reader (my_csv, delimiter = ',') #ogni riga è una lista. quindi posso prendere ogni elemento con gli indici[]
#table = csv.DictReader (dataset, delimiter =',') #aggiunge anche l'header ad ogni riga -- per chiamare gli elementi nelle righe non posso usare gli indici ma il nome che sta nell'header

#printo ogni riga nella tabella
#for row in table:
  #print (row) 
  #print (row['coordy'])
  
#creo una lista per l'header
header = ['id', 'coordx', 'coordy', 'h']
#creo una lista contenente tutte le altre righe del file. devo prima creare una lista vuota
lista = []
for row in tabella:  #per ogni riga della mia tabella
  lista.append(row) #aggiungi la riga alla mia lista vuota
print(lista) #ho la mia lista di liste
          
#creo un nuovo file csv  -- cambio il nome ma stessa directory!        
out_csv = open("/home/benedetta/Scrivania/UNIBO/LAB/montecristo_point_header.csv", 'w')
nuova_tabella = csv.writer (out_csv, delimiter = ',') #creo una nuova tabella 
#aggiungo l'header
nuova_tabella.writerow(header) #il comando è writerow, della libreria csv
#aggiungo la lista di liste
nuova_tabella.writerows(lista) #al plurale: writerows

print (nuova_tabella)

#devo sempre chiudere tutto dopo
my_csv.close()
out_csv.close()
print('FATTO')

#-----------------------------------------------------------------------------------------------------
import csv
my_data = open("/home/benedetta/Scrivania/UNIBO/LAB/montecristo_point.csv", 'r')
my_csv = csv.reader (my_data, delimiter =',')

#creo una lista vuota 
lista = []

#calcolo la quota ellissoidica
for row in my_csv:
  h_elips = int(row[3])+48
  print (h_elips)
  #devo aggiungere il valore di quota
  row.append (h_elips)
  #aggiungo tutto alla nuova lista
  lista.append(row)

#dato di output
out_data = open ("/home/benedetta/Scrivania/UNIBO/LAB/montecristo_point_elips.csv", 'w')
new_csv = csv.writer (out_data, delimiter =',')
new_csv.writerows(lista)

#chiudo tutto
my_data.close()
out_data.close()
print('FATTO') 


#-------------------------------------------------------------------------------------------------------------

#leggo il csv con pandas 
import pandas as pd
my_data = pd.read_csv ("/home/benedetta/Scrivania/UNIBO/LAB/montecristo_point_header.csv")
print(my_data)
#print(my_data['xcoord'])
#con il modulo pandas oggiungo molto semplicemente una colonna
my_data ['h_elips'] = my_data['h'] + 48
my_data.to_csv("/home/benedetta/Scrivania/UNIBO/LAB/montecristo_point_elips_pandas.csv")
print(my_data)
print ('FATTO')




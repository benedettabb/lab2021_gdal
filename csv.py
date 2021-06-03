import csv
#carico il dataset
dataset = open("C:/Users/UTENTE/Desktop/UNIBO/GEOGRAFIA/II ANNO/LAB/python/montecristo_point.csv")
#apro la tabella
table = csv.reader (dataset, delimiter = ',')

for row in table:
  print row


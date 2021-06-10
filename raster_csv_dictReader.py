from osgeo import gdal
import csv
#operation system - per inserire i percorsi
import os

os.chdir("/home/benedetta/Scrivania/UNIBO/LAB")



def sample_header(tabella, raster, csv_out):
  data = gdal.Open(raster)
  band = data.GetRasterBand(1)
  gt = data.GetGeoTransform()
  
  my_csv = open(tabella,'r')
  punti = csv.DictReader (my_csv, delimiter=',')
  lista =[]
  header =['id','luogo','stato','xcoord','ycoord','quota']
  for row in punti:
    #print(row)
    #creo una lista vuota
    list_row=[]
    #visto che uso il dict reader posso richiamare le colonne direttamente dall'header
    xcoord =row["xcoord"]
    ycoord =row["ycoord"]
    px = int((xcoord-gt[0])/gt[1]) #il valore di coordinata su una matrice deve essere un numero intero
    py = int((ycoord-gt[3])/gt[5])
    #fin'ora è praticamente tutto uguale a prima
    #ora rispario una riga -- prima leggi band come una matrice e poi individuo la quota tramite gli indici
    #1, 1 sta per l'estensione
    quota = band.ReadAsArray(px, py, 1,1)
    #print(quota)
    list_row.append(row['id'])
    list_row.append(row['luogo'])
    list_row.append(row['stato'])
    list_row.append(row['xcoord'])
    list_row.append(row['ycoord'])
    list_row.append(row['quota'])
    list_row.append(quota)
    lista.append(list_row)
  print(lista)
  
  new_csv =open(csv_out, 'w')
  writer = csv.writer(new_csv, delimiter=',')
  writer.writerow(header)
  writer.writerows(lista)
  
  data=None
  my_csv.close()
  csv_out.close()
    
#chiamo la funzione
#uso il file csv con gli header!!
sample_header ("points_pianosa.csv", "pianosa_dem.tif", "points_pianosa_quota_dict.csv")
    

from osgeo import gdal
import csv
#il raster di pianosa ha data type= float32. con gdal_traslate si può combiare la tipologia
#salvabile nel raster.
#risoluzione = 10mx10m

def sample (tabella, raster, csv_out):
    #apro il raster
    data = gdal.Open(raster)
    #devo leggere il raster come un array
    #prima devo ottenere i valori scritti nel raster - in questo caso c'è solo una banda (la quota)
    band = data.GetRasterBand(1)
    band_arr = band.ReadAsArray()
    #print(band_arr)
    #devo passare dalle coordinate xy alle coordinate pixel
    gt = data.GetGeoTransform()
    #gt è una tupla, una specie di lista 
    print(gt)
    
    
    #apro il csv in modalità di lettura 'r'
    my_csv = open(tabella,'r')
    #uso il reader per leggere il csv -- il delimiter è di default ,
    punti = csv.reader(my_csv, delimiter = ',')
    #apro intanto una lista vuota
    lista = []
    #aggiungo l'header
    header = ['id', 'luogo','stato', 'xcoord','ycoord','quota']
    #uso un ciclo for -- per ogni riga nel csv
    for row in punti:
        #print(row) #così mi stampa tutte le righe
        #la coordinata x è uguale all'indice 3 del csv
        xcoord = float(row[3]) #inserisco float perchè altrimenti avrei i valori in stringa
        #la coordinata y è al 4 posto
        ycoord =float(row[4])
        #print (xcoord, ycoord) #mi stampa le due colonne delle coordinate x e y
        #formula che mette in relazione il valore di coordinata con la risoluzione
        #dalle coordinate xy ricavo le coordinate relative all'immagine
        px = int((xcoord-gt[0])/gt[1]) #il valore di coordinata su una matrice deve essere un numero intero
        py = int((ycoord-gt[3])/gt[5])
        #ora devo dirgi di andare a prendere il valore di coord x e y sull'array che ho definito prima
        quota = band_arr[py,px]
        print(quota)
        #ora devo creare un nuovo csv che abbia anche il valore di queste quote
        row.append (quota)
        #aggiungo tutto alla lista vuota
        lista.append(row)
    #creo un nuovo csv
    new_csv = open(csv_out, 'w')
    #lo scrivo con il modulo csv.writer
    writer = csv.writer (new_csv, delimiter =',')
    #aggiungo l'header
    writer.writerow(header)
    #aggiungo tutte le liste
    writer.writerows(lista)
    
    #chiudo tutto
    data = None
    my_csv.close()
    new_csv.close()
 
#chiamo la funzione
sample ("/home/benedetta/Scrivania/UNIBO/LAB/points_pianosa_noHeader.csv", "/home/benedetta/Scrivania/UNIBO/LAB/pianosa_dem.tif", "/home/benedetta/Scrivania/UNIBO/LAB/points_pianosa_quota.csv")



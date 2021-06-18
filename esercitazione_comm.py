#importo i moduli
from osgeo import gdal #per i raster
from osgeo import ogr #per i vettori
from osgeo  import osr #modulo di gdal che gestisce proiezioni, riproiezioni ecc
import glob #da globale - per lavorare su più file in una cartella, es per cercare un pattern specifico
import os #per definire la cartella di lavoro
import csv #per lavorare sui csv

#definisco la cartella di lavoro
os.chdir("/home/benedetta/Scrivania/UNIBO/LAB/esercitazione_python/esercitazione")

'''funzione che prende due parametri - csv e raster - e restiuisce:
     - uno shapefile per ogni csv, a cui è aggiunto il valore di quota misurato sul raster
     - nuovi csv con l'aggiunta dell'info di quota '''
     
def sample (csv_file, raster):
    #APRO IL CSV
    csvfile_read = open (csv_file, 'r')
    reader = csv.DictReader (csvfile_read, delimiter = ',') #metodo DictReader (permette di richiamare le colonne usando l'header)
    
    
    #APRO IL RASTER
    dem = gdal.Open (raster) #apro il raster con Open della libreria gdal
    gt = dem.GetGeoTransform() #ottengo GeoTransform (output= tupla)
    num_bands = dem.RasterCount #controllo il numero di bande (1)
    print(num_bands)
    band = dem.GetRasterBand(1) #prendo la prima banda del raster
    #print(type(band))
    
    #SHAPE FILE
    name_shape = csv_file.split ('.')[0] + '_quota.shp' #il nome del nuovo shape sarà come quello del csv + _quota.shp
    driver = ogr.GetDriverByName('ESRI Shapefile') #preparo il driver
    data_source = driver.CreateDataSource(name_shape) #creo lo shapefile
    srs = osr.SpatialReference() #creo il sistema di riferimento
    srs.ImportFromEPSG(32632) #assegno l'EPSG:32632 UTM 32N come sistema di riferimento
    layer = data_source.CreateLayer(name_shape,srs,ogr.wkbPoint) #creo il layer definendo: nome, sistema di riferimento e tipologia di geometria (wkbPoint)

    #definisco i campi 
    field_reg = ogr.FieldDefn ('COD_REG', ogr.OFTInteger)
    layer.CreateField (field_reg)
    field_cm = ogr.FieldDefn ('COD_CM', ogr.OFTInteger)
    layer.CreateField (field_cm)
    field_pro = ogr.FieldDefn ('COD_PRO', ogr.OFTInteger)
    layer.CreateField (field_pro)
    field_com = ogr.FieldDefn ('PRO_COM', ogr.OFTInteger)
    layer.CreateField (field_com)
    field_comune= ogr.FieldDefn ('COMUNE', ogr.OFTString)
    field_comune.SetWidth (100) #nel caso di stringhe devo definirne la lunghezza
    layer.CreateField(field_comune)
    field_nome_ted= ogr.FieldDefn ('NOME_TED', ogr.OFTString)
    field_nome_ted.SetWidth (100)
    layer.CreateField(field_nome_ted)
    field_flag_cm = ogr.FieldDefn ('FLAG_CM', ogr.OFTInteger)
    layer.CreateField (field_flag_cm)
    field_shape_leng = ogr.FieldDefn ('SHAPE_Leng', ogr.OFTReal) #float
    layer.CreateField (field_shape_leng)
    field_shape_area = ogr.FieldDefn ('SHAPE_Area', ogr.OFTReal)
    layer.CreateField (field_shape_area)
    field_xcoord = ogr.FieldDefn ('xcoord', ogr.OFTReal)
    layer.CreateField (field_xcoord)
    field_ycoord = ogr.FieldDefn ('ycoord', ogr.OFTReal)
    layer.CreateField (field_ycoord)
    field_quota = ogr.FieldDefn ('quota', ogr.OFTReal)
    layer.CreateField (field_quota)
    
    #definisco l'header che inserirò nel nuovo csv
    fields = ['COD_REG', 'COD_CM', 'COD_PRO', 'PRO_COM', 'COMUNE', 'NOME_TED', 'FLAG_CM', 'SHAPE_Leng', 'SHAPE_Area', 'xcoord', 'ycoord','quota']
    lista = [] #creo una lista vuota che conterrà tutte le colonne del nuovo csv

    for row in reader: #apro un ciclo for: per ogni riga del csv
        list_row = [] #altra lista vuota che conterrà le righe del csv già presenti
        utm_x = float(row['xcoord']) #ottengo il valore della coordinata X presente nel csv
        utm_y = float(row['ycoord']) #ottengo il valore della coordinata Y presente nel csv
        px = int((utm_x-gt[0])/gt[1]) #passaggio che mi permette di ottenere la coordinata X in pixel sul raster  - è un intero perché si riferisce al pixel
        py = int((utm_y-gt[3])/gt[5]) #passaggio che mi permette di ottenere la coordinata Y in pixel sul raster
        quota = band.ReadAsArray(px,py, 1, 1) #leggo il valore di quota come una matrice
        q = float(quota) #scrivo la quota come float
        #print(q)

        #shape file:
        feature = ogr.Feature (layer.GetLayerDefn()) #definisco la feature, ossiauna riga che compone la tabella attributi dello shape su qgis
        feature.SetField ('COD_REG', row['COD_REG']) #definisco il valore del campo COD_REG creato sopra associando il valore della colonna COD_REG del csv
        feature.SetField ('COD_CM', row['COD_CM']) #per tutti i campi
        feature.SetField ('COD_PRO', row['COD_PRO'])
        feature.SetField ('PRO_COM', row['PRO_COM'])
        feature.SetField ('COMUNE', row['COMUNE'])
        feature.SetField ('NOME_TED', row['NOME_TED'])
        feature.SetField ('FLAG_CM', row['FLAG_CM'])
        feature.SetField ('SHAPE_Leng', row['SHAPE_Leng'])
        feature.SetField ('SHAPE_Area', row['SHAPE_Area'])
        feature.SetField ('xcoord', row['xcoord'])
        feature.SetField ('ycoord', row['ycoord'])
        feature.SetField ("quota", q) #inserisco il campo quota calcolato sul raster
        
        wkt = "POINT (%f %f)" % (float(row['xcoord']), float (row['ycoord'])) #uso il linguaggio wkt per scrivere la stringa - uso una geometria puntuale
        #print(wkt)
        #creo la geometria dal wkt
        point = ogr.CreateGeometryFromWkt (wkt) #creo la geometrica dal wkt
    
      
        feature.SetGeometry (point) #setto il valore della geometria sulla feature
        layer.CreateFeature(feature) #inserisco la geometria nel layer
    
        #csv: aggiungo alla lista vuota (nel ciclo for) le colonne del csv parametro della funzione
        list_row.append(row['COD_REG'])
        list_row.append(row ['COD_CM'])
        list_row.append(row ['COD_PRO'])
        list_row.append(row ['PRO_COM'])
        list_row.append(row ['COMUNE'])
        list_row.append(row ['NOME_TED'])
        list_row.append(row ['FLAG_CM'])
        list_row.append(row ['SHAPE_Leng'])
        list_row.append(row ['SHAPE_Area'])
        list_row.append(row ['xcoord'])
        list_row.append(row ['ycoord'])
        list_row.append (q) #aggiungo anche la colonna della quota ricavata dal dem
        lista.append(list_row) #aggiungo le liste alla lista vuota definita prima del ciclo for 
        
        feature = None #chiudo la feature riferita allo shapefile
        
    name = csv_file.split('.')[0] + '_quota.csv' #definisco il nome del csv a partire da quello già esistente
    new_csv = open (name,'w') #apro il csv con la modalità scrittura
    writer = csv.writer (new_csv) #apro il writer
    writer.writerow (fields) #scrivo l'header
    writer.writerows (lista) #scrivo la lista di liste
    
    
    data_source = None #chiudo il data source riferito allo shape
    csvfile_read.close()  #chiudo il reader del csv
    new_csv.close() #chiudo il csv creato

gdal.Warp('dem_lombardia_100m_WGS.tif', 'dem_lombardia_100m_ED32N.tif', dstSRS = 'EPSG:32632') #riproietto il dem nel sistema dei csv (UTM WGS84)

#apro un ciclo for: per ogni csv nella cartella -ossia ogni file che finisce con csv
for csv_file in glob.glob ('*csv'):
    sample (csv_file, 'dem_lombardia_100m_WGS.tif') #applico la funzione con argomenti (ogni csv nella cartella, il raster riproiettato)
print ('fatto?') 




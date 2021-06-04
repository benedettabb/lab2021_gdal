#il nostro scopo è calcolare la quota nel file dem
#e inserire quella colonna nel file csv

#-------GDAL--------------------------------------------------------
#documentation -----GDAL Cookbook------------------------
from osgeo import gdal #------------> dati raster
from osgeo import ogr  #------------> dati vettoriali

my_data = gdal.Open('/home/benedetta/Scrivania/UNIBO/LAB/pianosa_dem.tif')
print (my_data)
print(type(my_data)) # è un tipo di gdal
print(my_data.GetMetadata())  #metadati del raster

#prendo la prima (e unica) banda del DEM
band = my_data.GetRasterBand(1)
#gli dico di leggere la banda come un array
band_value = band.ReadAsArray()
print(band_value)
#mi stampa i valori di DN come una matrice ---non tutti ovviamente
#stampa i 4 angoli dell'immagine
print(band_value[400,450]) #-----coordinate del pixel di cui mi stampa il valore
#posso ottenere tutti i riferimenti spaziali del raster
spatial = my_data.GetSpatialRef()
print (str(spatial)) #le posso far gestire come una stringa
gt = my_data.GetGeoTransform()
print(gt)

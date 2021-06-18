from osgeo import gdal
from osgeo import ogr
from osgeo  import osr
import glob
import os
import csv
import numpy

os.chdir('C:/Users/UTENTE/Desktop/UNIBO/GEOGRAFIA/II ANNO/LAB/esercitazione_python/esercitazione')

def sample (csv_file, raster):
    #APRO IL CSV
    csvfile_read = open (csv_file, 'r')
    reader = csv.DictReader (csvfile_read, delimiter = ',')
    
    
    #APRO IL RASTER
    dem = gdal.Open (raster)
    gt = dem.GetGeoTransform()
    num_bands = dem.RasterCount#View the number of bands
    print(num_bands)
    band = dem.GetRasterBand(1)
    #print(type(band))
    
    #NUOVI SHAPE FILE
    #assegno il nome a partire dal csv
    name_shape = csv_file.split ('.')[0] + '_quota.shp' #il nome del nuovo shape sarà come quello precedente + quota
    driver = ogr.GetDriverByName('ESRI Shapefile') #preparo il driver
    data_source = driver.CreateDataSource(name_shape) #creo lo shapefile
    srs = osr.SpatialReference() #creo il sistema di riferimento
    srs.ImportFromEPSG(32632) #assegno l'EPSG:32632 UTM 32N come sistema di riferimento
    layer = data_source.CreateLayer(name_shape,srs,ogr.wkbPoint) #creo il layer definenedo: nome, sistema di riferimento e tipologia di geometria (wkbPoint)

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
    field_comune.SetWidth (100)
    layer.CreateField(field_comune)
    field_nome_ted= ogr.FieldDefn ('NOME_TED', ogr.OFTString)
    field_nome_ted.SetWidth (100)
    layer.CreateField(field_nome_ted)
    field_flag_cm = ogr.FieldDefn ('FLAG_CM', ogr.OFTInteger)
    layer.CreateField (field_flag_cm)
    field_shape_leng = ogr.FieldDefn ('SHAPE_Leng', ogr.OFTReal)
    layer.CreateField (field_shape_leng)
    field_shape_area = ogr.FieldDefn ('SHAPE_Area', ogr.OFTReal)
    layer.CreateField (field_shape_area)
    field_xcoord = ogr.FieldDefn ('xcoord', ogr.OFTReal)
    layer.CreateField (field_xcoord)
    field_ycoord = ogr.FieldDefn ('ycoord', ogr.OFTReal)
    layer.CreateField (field_ycoord)
    field_quota = ogr.FieldDefn ('quota', ogr.OFTReal)
    layer.CreateField (field_quota)
    
    
    fields = ['COD_REG', 'COD_CM', 'COD_PRO', 'PRO_COM', 'COMUNE', 'NOME_TED', 'FLAG_CM', 'SHAPE_Leng', 'SHAPE_Area', 'xcoord', 'ycoord','quota']
    lista = []

    for row in reader:
        list_row = []
        utm_x = float(row['xcoord']) #ottengo il valore della coordinata X presente nel csv
        utm_y = float(row['ycoord']) #ottengo il valore della coordinata Y presente nel csv
        px = int((utm_x-gt[0])/gt[1]) #passaggio che mi permette di ottenere la coordinata X in pixel sul raster
        py = int((utm_y-gt[3])/gt[5]) #passaggio che mi permette di ottenere la coordinata Y in pixel sul raster
        quota = band.ReadAsArray(px,py, 1, 1)
        q = float(quota)
        #print(q)
        
        feature = ogr.Feature (layer.GetLayerDefn())
        feature.SetField ('COD_REG', row['COD_REG'])
        feature.SetField ('COD_CM', row['COD_CM'])
        feature.SetField ('COD_PRO', row['COD_PRO'])
        feature.SetField ('PRO_COM', row['PRO_COM'])
        feature.SetField ('COMUNE', row['COMUNE'])
        feature.SetField ('NOME_TED', row['NOME_TED'])
        feature.SetField ('FLAG_CM', row['FLAG_CM'])
        feature.SetField ('SHAPE_Leng', row['SHAPE_Leng'])
        feature.SetField ('SHAPE_Area', row['SHAPE_Area'])
        feature.SetField ('xcoord', row['xcoord'])
        feature.SetField ('ycoord', row['ycoord'])
        feature.SetField ("quota", q)
        
        wkt = "POINT (%f %f)" % (float(row['xcoord']), float (row['ycoord']))
        #print(wkt)
        #creo la geometria dal wkt
        point = ogr.CreateGeometryFromWkt (wkt)
    
        #ora devo settare il valore della geometria sulla feature
        feature.SetGeometry (point)
        #inserisco la geometria nel layer
        layer.CreateFeature(feature)
    

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
        list_row.append (q)
        lista.append(list_row)
        
        #chiudo la feature
        feature = None
        
    name = csv_file.split('.')[0] + '_quota.csv'
    new_csv = open (name,'w')
    writer = csv.writer (new_csv)
    writer.writerow (fields)
    writer.writerows (lista)
    
    #chiudo il data source
    data_source = None
    csvfile_read.close()
    new_csv.close()

gdal.Warp('dem_lombardia_100m_WGS.tif', 'dem_lombardia_100m_ED32N.tif', dstSRS = 'EPSG:32632')


for csv_file in glob.glob ('*csv'):
    sample (csv_file, 'dem_lombardia_100m_WGS.tif')
print ('fatto?')



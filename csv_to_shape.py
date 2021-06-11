import csv
import  os
from osgeo import gdal
from osgeo import ogr
from osgeo import osr

os.chdir ("/home/benedetta/Scrivania/UNIBO/LAB/ultima_lezione")

#apro csv
my_csv = open ("rio_nell_elba.csv", "r")
reader = csv.DictReader (my_csv, delimiter =',')

#ciclo su ogni colonna per leggere il valore del raster
#apro raster
raster = gdal.Open("elba_dem_utm.tif")
gt = raster.GetGeoTransform()
band = raster.GetRasterBand (1)

#bisogna usare ogr. creo un nuovo file, associato alla variabile driver
#driver => sto per creare il file vettoriale
driver = ogr.GetDriverByName ('ESRI Shapefile')

#creo il data source dal driver --creo il file
data_source = driver.CreateDataSource ('rio_nell_elba_shape.shp')

#devo creare il layer (che è contenuto nello shapefile)
#il layer ha bisogno di info spaziali
#definisco il sistema di riferimento
srs =osr.SpatialReference() #osr è il modulo che consente di creare i sistemi di riferimento
#srs è una variabile spatial reference, sui cui stabilisco il sistema di riferimento
srs.ImportFromEPSG(32632)

#creo il layer, devo inserire il nome, il sistema di riferimento, la geometria(punti in questo caso)
layer = data_source.CreateLayer("rio_nell_elba_shape", srs, ogr.wkbPoint)

#definisco il campo
field_fid =ogr.FieldDefn ("fid", ogr.OFTString) #nel caso della stringa devo anche definire la lunghezza del campo
#definisco la lunghezza del campo
field_fid.SetWidth (100)
#creo il campo
layer.CreateField (field_fid)

field_full_id =ogr.FieldDefn ("full_id", ogr.OFTString)
field_full_id.SetWidth (100)
layer.CreateField (field_full_id)

field_osm_id =ogr.FieldDefn ("osm_id", ogr.OFTString)
field_osm_id.SetWidth (100)
layer.CreateField (field_osm_id)

field_osm_type =ogr.FieldDefn ("osm_type", ogr.OFTString)
field_osm_type.SetWidth (100)
layer.CreateField (field_osm_type)

field_name =ogr.FieldDefn ("name", ogr.OFTString)
field_name.SetWidth (100)
layer.CreateField (field_name)

field_natural =ogr.FieldDefn ("natural", ogr.OFTString)
field_natural.SetWidth (100)
layer.CreateField (field_natural)

field_xcoord =ogr.FieldDefn ("xcoord", ogr.OFTReal)
layer.CreateField (field_xcoord)

field_ycoord =ogr.FieldDefn ("ycoord", ogr.OFTReal)
layer.CreateField (field_ycoord)

field_quota =ogr.FieldDefn ("quota", ogr.OFTReal)
layer.CreateField (field_quota)

# GRANDE CICLO FOR
#inserisco i valori di quota letto sul raster
for row in reader:
    xcoord =float(row["xcoord"])
    ycoord =float(row["ycoord"])
    px = int((xcoord-gt[0])/gt[1]) 
    py = int((ycoord-gt[3])/gt[5])
    quota = band.ReadAsArray(px, py, 1,1)
    q=float(quota)

    #vado a scrivere i valori di quota nello shape file
    #creo la feature, ossia il punto
    feature = ogr.Feature (layer.GetLayerDefn())
    feature.SetField ("fid", row["fid"])
    feature.SetField ("full_id", row["full_id"])
    feature.SetField ("osm_id", row["osm_id"])
    feature.SetField ("osm_type", row["osm_type"])
    feature.SetField ("name", row["name"])
    feature.SetField ("natural", row["natural"])
    feature.SetField ("xcoord", row["xcoord"])
    feature.SetField ("ycoord", row["ycoord"])
    feature.SetField ("quota", q)

    #ora devo effettivamente creare la feature con la modalità wkt (well known text)
    #wkt è un linguaggio creato per rapp oggetti vettoriali nelle mappe
    wkt = "POINT (%f %f)" % (float(row['xcoord']), float (row['ycoord']))
    print(wkt)

    #creo la geometria dal wkt
    point = ogr.CreateGeometryFromWkt (wkt)
    
    #ora devo settare il valore della geometria sulla feature
    feature.SetGeometry (point)
    #inserisco la geometria nel layer
    layer.CreateFeature(feature)
    #chiudo la feature
    feature = None
    
#chiudo il data source
data_source = None

print("shapefile creato")



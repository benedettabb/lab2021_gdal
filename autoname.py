
import csv
from osgeo import gdal
#mi permette di impostare la cartella di lavoro
import os
#modulo che permette di fare cicli all'interno della cartella di lavoro
import glob

#definisco la cartella di lavoro
os.chdir("/home/benedetta/Scrivania/UNIBO/LAB/ultima_lezione")

#due parametri, csv e dem -- in nome del nuovo csv verrà definito
#all'interno della funzione
def sample (csv_file, raster):  
    csvfile_read = open(csv_file,'r')
    reader = csv.DictReader(csvfile_read, delimiter = ',')

    dem = gdal.Open(raster)
    gt = dem.GetGeoTransform()
    band = dem.GetRasterBand(1)

    fields = ['fid','full_id','osm_id','osm_type','name','natural','xcoord','ycoord','quota']
    lista = []

    for row in reader:
        list_row = []
        utm_x = float(row['xcoord'])
        utm_y = float(row['ycoord'])
        px = int((utm_x-gt[0])/gt[1])  
        py = int((utm_y-gt[3])/gt[5])
        quota = band.ReadAsArray(px,py,1,1)
        q = quota

        list_row.append(row['fid'])
        list_row.append(row['full_id'])
        list_row.append(row['osm_id'])
        list_row.append(row['osm_type'])
        list_row.append(row['name'])
        list_row.append(row['natural'])
        list_row.append(row['xcoord'])
        list_row.append(row['ycoord'])      
        list_row.append(q)
        lista.append(list_row)

    name = csv_file.split('.')[0] + '_quota.csv'
    csvfile_write = open(name,'w') 
    writer = csv.writer(csvfile_write)
    writer.writerow(fields) 
    writer.writerows(lista)
    csvfile_read.close()
    csvfile_write.close()


gdal.Warp ('elba_dem_utm.tif', 'elba_dem.tif', dstSRS = 'EPSG:32632')
print('fatto')

#applico questa funzione a tutti i file nella cartella che finiscono con .csv
for csv_file in glob.glob ('*.csv'):
    sample (csv_file, "elba_dem_utm.tif")
print("The end")

#sample ("marciana.csv", "elba_dem.tif")

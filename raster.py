from osgeo import gdal
import csv
#il raster di pianosa ha data type= float32. con gdal_traslate si può combiare la tipologia
#salvabile nel raster.
#risoluzione = 10mx10m

def sample (tabella, raster):
    data = gdal.Open(raster)
    band = data.GetRasterBand(1)
    band_arr = band.ReadAsArray()
    print(band_arr)

    my_csv = open(tabella,'r')
    punti = csv.reader(my_csv, delimiter = ',')
    for row in punti:
        xcoord = row[3]
        ycoord =row[4]

sample ("/home/benedetta/Scrivania/UNIBO/LAB/points_pianosa_noHeader.csv", "/home/benedetta/Scrivania/UNIBO/LAB/pianosa_dem.tif")



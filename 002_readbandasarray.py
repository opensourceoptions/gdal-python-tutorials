import gdal

fn = "C:/temp/elevation/ned10m.tif"
ds = gdal.Open(fn) #open a raster dataset

band1 = ds.GetRasterBand(1).ReadAsArray() #read band 1 as a numpy array
print(band1.shape) #shape of array (rows, columns)
print(band1.mean())
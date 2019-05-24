import gdal

fn = "C:/temp/new_raster.tif"

ds = gdal.Open(fn)

#print basic raster info
print(ds.RasterXSize, ds.RasterYSize) #number of columns and rows
print(ds.GetProjection()) #projection info
print(ds.GetGeoTransform()) #geotransform info
print("Number of raster bands", ds.RasterCount) #number of bands/layer in raster

#print raster band info
band1 = ds.GetRasterBand(1)
print("No data value", band1.GetNoDataValue()) #no data value
print("min value", band1.GetMinimum()) #minimum value
print("max value", band1.GetMaximum()) #maximum value
print("data type", band1.GetUnitType()) #unit type (integer, float, etc.)


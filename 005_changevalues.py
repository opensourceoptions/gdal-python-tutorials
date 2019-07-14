import gdal

fn = "C:/temp/test.tif" #new raster
fn_template = "C:/temp/elevation/ned10m.tif" #template raster

ds_temp = gdal.Open(fn_template) #open template raster
driver_tiff = gdal.GetDriverByName("Gtiff") #Get geotiff driver

#create new dataset
ds = driver.Create(fn, xsize=10, ysize=10,\
bands=1, eType=gdal.GDT_Float32)

ds.SetGeoTransform(ds_temp.GetGeoTransform) #set geotransform to match template raster
ds.SetProjection(ds_temp.GetProjection) #set projection

band1 = ds.GetRasterBand(1).ReadAsArray() #read the raster band as an array
band1[0][1] = 100.0 #change the value of the first row, second column
band1[1][2] = 50.0 #change the value of the second row, third column
ds.GetRasterBand(1).WriteArray(band1) #write array with changed values to the raster band

ds = None #close the raster datasetCount

iface.addRasterLayer(fn) #add raster to the QGIS interface

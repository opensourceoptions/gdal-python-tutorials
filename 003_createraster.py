import gdal

#new raster filename
fn = "C:/temp/new_raster.tif"
#existing raster filename
fn2 = "C:/temp/elevation/ned10m.tif"
#open existing raster
ds = gdal.Open(fn2)
#get the geotransform and projection of an existing raster
geot = ds.GetGeoTransform()
proj = ds.GetProjection()
#get a gdal driver to use for raster creation
driver_tiff = gdal.GetDriverByName("GTiff")
#create the new raster dataset
new_ds = driver_tiff.Create(fn, xsize=ds.RasterXSize,\
ysize=ds.RasterYSize, bands=1,\
eType=gdal.GDT_Float32)
#set the geotransform
new_ds.SetGeoTransform(geot)
#set the projection
new_ds.SetProjection(proj)
del(new_ds)
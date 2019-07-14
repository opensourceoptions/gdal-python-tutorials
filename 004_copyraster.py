import gdal

fn = "C:/temp/elevation/ned10m.tif" #original file
fn_new = "C:/temp/ned10m_copy.tif"  #new file

#open the original file
ds = gdal.Open(fn)

#get a gdal driver
driver_tiff = gdal.GetDriverByName("GTiff")

#create a copy of the original raster
ds_copy = driver_tiff.CreateCopy(fn_new, ds, strict=0)

#properly close the new dataset
ds_copy = None

#add new raster to qgis
iface.addRasterLayer(fn_new)

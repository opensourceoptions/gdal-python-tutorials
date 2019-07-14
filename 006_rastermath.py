import gdal

#file names for existing raster and two new rasters
fn_template = "C:/temp/elevation/ned10m.tif"
fn_new = "C:/temp/new_raster.tif"
fn_dif = "C:/temp/dif_raster.tif"

ds_template = gdal.Open(fn_template)

driver_tiff = gdal.GetDriverByName("GTiff")

#copy existing raster to create two new rasters
ds_new = driver_tiff.CreateCopy(fn_new, ds_template, strict=0)
ds_dif = driver_tiff.CreateCopy(fn_dif, ds_template, strict=0)

#read band from existing raster and multiply by 1.25 to create new raster
band_base = ds_template.GetRasterBand(1).ReadAsArray()
band_new = band_base * 1.25
band_dif = band_new - band_base #get the difference between new and existing raster

#write new data to the new rasters
ds_new.GetRasterBand(1).WriteArray(band_new)
ds_dif.GetRasterBand(1).WriteArray(band_dif)

#calculate statistics for the new rasters
ds_new.GetRasterBand(1).ComputeStatistics(0)
ds_dif.GetRasterBand(1).ComputeStatistics(0)

#close rasters
ds_template = None
ds_new = None
ds_dif = None

#add new rasters to interface
iface.addRasterLayer(fn_new)
iface.addRasterLayer(fn_dif)
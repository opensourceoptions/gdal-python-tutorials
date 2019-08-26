import gdal
import numpy as np

fn = "C:/temp/elevation/ned10m.tif"
newfn = "C:/temp/elevation/ned10m_nodata.tif"

driver = gdal.GetDriverByName("GTiff")
copyds = gdal.Open(fn)
ds = driver.CreateCopy(newfn, copyds, strict=0)

ds = gdal.Open(newfn, 1)
ndv = ds.GetRasterBand(1).GetNoDataValue()
newndv = -9999.0 # set new no data value
band1 = ds.GetRasterBand(1).ReadAsArray() # read raster band

band1[band1==ndv] = newndv # change no data value
#band1[band1==ndv] = np.nan # change no data value to nan

ds.GetRasterBand(1).SetNoDataValue(newndv) # specify new no data value for the raster band
ds.GetRasterBand(1).WriteArray(band1)

ds = None

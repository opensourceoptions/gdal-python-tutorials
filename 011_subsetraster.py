import gdal

fn = "C:/temp/elevation/ned10m.tif"
fn_clip = "C:/temp/elevation/ned10m_clip.tif"

# Example 1, top right corner stays the same
ds = gdal.Open(fn)
newRows = 500  # y coordinate
newCols = 500  # x coordinate

geot = ds.GetGeoTransform()

driver = gdal.GetDriverByName("GTiff")
ds_clip = driver.Create(fn_clip, xsize = newCols, ysize=newRows, \
bands=1, eType = gdal.GDT_Float32)

#ds_clip.SetGeoTransform(geot)
#
#data = ds.GetRasterBand(1).ReadAsArray()
#ds_clip.GetRasterBand(1).WriteArray(data[:newRows, :newCols])
#ds_clip.GetRasterBand(1).SetNoDataValue(ds.GetRasterBand(1).GetNoDataValue())

# Example 2, change top right corner

xOffset = 2500 # meters
yOffset = 3000 # meters

geotNew = list(geot)

geotNew[0] = geotNew[0] + xOffset
geotNew[3] = geotNew[3] - yOffset

ds_clip.SetGeoTransform(tuple(geotNew))
startRow = round(yOffset/abs(geot[5]))
startCol = round(xOffset/abs(geot[1]))

data = ds.GetRasterBand(1).ReadAsArray()
ds_clip.GetRasterBand(1).WriteArray(data[startRow:startRow+newRows,\
startCol:startCol+newCols])

ds_clip = None

iface.addRasterLayer(fn_clip)



import gdal

def openRaster(fn, access=0):
    ds = gdal.Open(fn, access)
    if ds is None:
        print("Error opening raster dataset")
    return ds

def getRasterBand(fn, band=1, access=0):
    ds = openRaster(fn, access)
    band = ds.GetRasterBand(1).ReadAsArray()
    return band

def createRasterFromCopy(fn, ds, data, driverFmt="GTiff"):
    driver=gdal.GetDriverByName(driverFmt)
    outds = driver.CreateCopy(fn, ds, strict=0)
    outds.GetRasterBand(1).WriteArray(data)
    ds = None
    outds = None

def subtractRasters(fn1, fn2, fnout):
    dat1 = getRasterBand(fn1)
    dat2 = getRasterBand(fn2)
    datout = dat2-dat1
    createRasterFromCopy(fnout, gdal.Open(fn1), datout)

fn1 = "C:/temp/elevation/ned10m.tif"
fn2 = "C:/temp/elevation/ned10m_altered.tif"
fnout = "C:/temp/elevation/subtract.tif"
subtractRasters(fn1, fn2, fnout)
iface.addRasterLayer(fnout)

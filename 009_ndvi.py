import gdal
import numpy as np

def openRaster(fn, access=0):
    ds = gdal.Open(fn, access)
    if ds is None:
        print("Error opening raster dataset")
    return ds

def getRasterBand(fn, band=1, access=0):
    ds = openRaster(fn, access)
    band = ds.GetRasterBand(band).ReadAsArray()
    return band

def createRasterFromCopy(fn, ds, data, driverFmt="GTiff"):
    driver=gdal.GetDriverByName(driverFmt)
    outds = driver.CreateCopy(fn, ds, strict=0)
    outds.GetRasterBand(1).WriteArray(data)
    ds = None
    outds = None

def createRasterFromTemplate(fn, ds, data, ndv=-9999.0, \
driverFmt="GTiff"):
    driver = gdal.GetDriverByName(driverFmt)
    outds = driver.Create(fn, xsize=ds.RasterXSize, ysize=ds.RasterYSize,\
    bands=1, eType=gdal.GDT_Float32)
    outds.SetGeoTransform(ds.GetGeoTransform())
    outds.SetProjection(ds.GetProjection())
    outds.GetRasterBand(1).SetNoDataValue(ndv)
    outds.GetRasterBand(1).WriteArray(data)
    outds = None
    ds = None
    
def ndvi(nirband, redband, ndv=-9999.0):
    nirband[nirband < 0] = np.nan
    nirband[nirband > 10000] = np.nan
    nirband[redband < 0] = np.nan
    nirband[redband > 10000] = np.nan
    ndviband = (nirband-redband)/(nirband+redband)
    ndviband[np.isnan(ndviband)]=ndv
    return ndviband

infn = "C:/temp/landsat/LC08_CU_007003_20190802_20190822_C01_V01.tif"
outfn = "C:/temp/landsat/ndvi.tif"
redband = getRasterBand(infn, 4)
nirband = getRasterBand(infn, 5)
ndviband = ndvi(nirband, redband)
createRasterFromTemplate(outfn, gdal.Open(infn), ndviband)

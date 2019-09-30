import gdal

fn = "C:/temp/elevation/ned10m.tif"
out = "C:/temp/elevation/ned10m_4326.tif"

gdal.Warp(out, fn, dstSRS="EPSG:4326", xRes=0.01, yRes=0.01)

iface.addRasterLayer(out)
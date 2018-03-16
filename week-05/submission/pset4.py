from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
import os

def process_string (st):
    """
    Parses Landsat metadata
    """
    return float(st.split(' = ')[1].strip('\n'))

def ndvi_calc(red, nir):
    """
    Calculate NDVI
    """
    return (nir - red) / (nir + red)

def emissivity_calc (pv, ndvi):
    """
    Calculates an estimate of emissivity
    """
    ndvi_dest = ndvi.copy()
    ndvi_dest[np.where(ndvi < 0)] = 0.991
    ndvi_dest[np.where((0 <= ndvi) & (ndvi < 0.2)) ] = 0.966
    ndvi_dest[np.where((0.2 <= ndvi) & (ndvi < 0.5)) ] = (0.973 * pv[np.where((0.2 <= ndvi) & (ndvi < 0.5)) ]) + (0.966 * (1 - pv[np.where((0.2 <= ndvi) & (ndvi < 0.5)) ]) + 0.005)
    ndvi_dest[np.where(ndvi >= 0.5)] = 0.973
    return ndvi_dest

def array2tif(raster_file, new_raster_file, array):
    """
    Writes 'array' to a new tif, 'new_raster_file',
    whose properties are given by a reference tif,
    here called 'raster_file.'
    """
    # Invoke the GDAL Geotiff driver
    raster = gdal.Open(raster_file)

    driver = gdal.GetDriverByName('GTiff')
    out_raster = driver.Create(new_raster_file,
                        raster.RasterXSize,
                        raster.RasterYSize,
                        1,
                        gdal.GDT_Float32)
    out_raster.SetProjection(raster.GetProjection())
    # Set transformation - same logic as above.
    out_raster.SetGeoTransform(raster.GetGeoTransform())
    # Set up a new band.
    out_band = out_raster.GetRasterBand(1)
    # Set NoData Value
    out_band.SetNoDataValue(-1)
    # Write our Numpy array to the new band!
    out_band.WriteArray(array)


    def tif2array(location):
    """
    Should:
    1. Use gdal.open to open a connection to a file.
    2. Get band 1 of the raster
    3. Read the band as a numpy array
    4. Convert the numpy array to type 'float32'
    5. Return the numpy array.
    """
    data_path = os.path.join(location)
    data = gdal.Open(data_path)
    band = data.GetRasterBand(1)
    band_array = band.ReadAsArray()
    array = band_array.astype(np.float32)
    return array


def retrieve_meta(meta_text):
    """
    Retrieve variables from the Landsat metadata *_MTL.txt file
    Should return a list of length 4.
    'meta_text' should be the location of your metadata file
    Use the process_string function we created in the workshop.
    """
    with open(meta_text) as f:
        meta = f.readlines()
    matchers = ['RADIANCE_MULT_BAND_10', 'RADIANCE_ADD_BAND_10', 'K1_CONSTANT_BAND_10', 'K2_CONSTANT_BAND_10']
    matching = [process_string(s) for s in meta if any(xs in s for xs in matchers)]

    return matching


def rad_calc(tirs, var_list):
    """
    Calculate Top of Atmosphere Spectral Radiance
    Note that you'll have to access the metadata variables by
    their index number in the list, instead of naming them like we did in class.
    """
    rad = var_list[0] * tirs + var_list[1]
    return rad


def bt_calc(rad, var_list):
    """
    Calculate Brightness Temperature
    Again, you'll have to access appropriate metadata variables
    by their index number.
    """
    bt = var_list[3] / np.log((var_list[2]/rad) + 1) - 273.15
    return bt


def pv_calc(ndvi, ndvi_s, ndvi_v):
    """
    Calculate Proportional Vegetation
    """
    pv = (ndvi - ndvi_s) / (ndvi_v - ndvi_s) ** 2
    return pv


def lst_calc(location):

    var_list = retrieve_meta(location +"/" + 'LC08_L1TP_012031_20170716_20170727_01_T1_MTL.txt')
    tirs = tif2array(location +"/" + 'LC08_L1TP_012031_20170716_20170727_01_T1_B10.TIF')
    rad = rad_calc(tirs, var_list)
    bt = bt_calc(rad, var_list)

    red = tif2array(location +"/" + 'LC08_L1TP_012031_20170716_20170727_01_T1_B4.TIF')
    nir = tif2array(location +"/" + 'LC08_L1TP_012031_20170716_20170727_01_T1_B5.TIF')
    ndvi = ndvi_calc(red, nir)
    ndvi_s = 0.2
    ndvi_v = 0.5
    pv = pv_calc(ndvi, ndvi_s, ndvi_v)
    emis = emissivity_calc(pv, ndvi)

    wave = 10.8E-06
    h = 6.626e-34
    c = 2.998e8
    s = 1.38e-23
    p = h * c / s

    lst = bt / (1 + (wave * bt / p) * np.log(emis))
    return lst

# cloud_filter
bqa = tif2array(location + "/" + 'LC08_L1TP_012031_20170716_20170727_01_T1_BQA.tif')
def cloud_filter(array, bqa):
    array_dest = array.copy()
    array_dest[np.where((bqa != 2720) & (bqa != 2724)& (bqa != 2728)& (bqa != 2732)) ] = 'nan'
    return array_dest

# ndvi

location = "C:/Users/yueha/BigData/Landsat Data/LC08_L1TP_012031_20170716_20170727_01_T1"
red = tif2array(location +"/" + 'LC08_L1TP_012031_20170716_20170727_01_T1_B4.TIF')
nir = tif2array(location +"/" + 'LC08_L1TP_012031_20170716_20170727_01_T1_B5.TIF')
ndvi = ndvi_calc(red, nir)
# filter
ndvi_filter = cloud_filter(ndvi, bqa)
# plot
plt.imshow(ndvi_filter, cmap='YlGn')
plt.colorbar()
# export
tirs_path = os.path.join(location, 'LC08_L1TP_012031_20170716_20170727_01_T1_B4.TIF')
out_path = os.path.join(location, 'yuehan_ndvi_20170716.tif')
array2tif(tirs_path, out_path, ndvi_filter)

# lst
lst = lst_calc(location)
# filter
lst_filter = cloud_filter(lst, bqa)
# plot
plt.imshow(lst_filter, cmap='RdYlGn')
plt.colorbar()
# export
tirs_path = os.path.join(location, 'LC08_L1TP_012031_20170716_20170727_01_T1_B4.TIF')
out_path = os.path.join(location, 'yuehan_lst_20170716.tif')
array2tif(tirs_path, out_path, lst_filter)

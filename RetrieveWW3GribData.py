#-------------------------------------------------------------------------------
# Name:  Retrieve WW3 MultiGrid Global Data from NOMADS
# Purpose: Downloads a Grib file From NOAA NOMADS
# Author:      John Fry
#               DC Technology Office, Defense Team
# Created:     12/30/2014
# Copyright:   (c) john6807 2014
# Licence:     <your licence>
# Updated 1/25/15 for multi-grid changes in NOAA's website
#-------------------------------------------------------------------------------

#Modules


import  os , sys, urllib.request, time, datetime, arcpy

# What Python?
sysver = sys.version
arcpy.AddMessage(sysver)

# Prepare folders
scriptPath = sys.path[0]
downloadfolder = str(os.path.join(scriptPath) + r"\scratch\WW3")




#Base Url where GRIB2 data resides
#urlNWW31 = "http://nomads.ncep.noaa.gov/cgi-bin/filter_wave_multi.pl?file=multi_1.glo_30mext.t00z.f000.grib2&all_lev=on&all_var=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fmulti_1."
urlNWW31 = "http://nomads.ncep.noaa.gov/pub/data/nccf/com/wave/prod/multi_2."
urlNWW32= "/multi_2.glo_30m.t00z.grib2"
#Get UTC Date
#utctime = str(datetime.datetime.utcnow())
localtime = str(datetime.datetime.now())
#formatutc = time.strftime('%Y%m%d',time.strptime(utctime,"%Y-%m-%d %H:%M:%S.%f"))
formatlocal = time.strftime('%Y%m%d',time.strptime(localtime,"%Y-%m-%d %H:%M:%S.%f"))
#dlWW3data = str(downloadfolder + r"\multi_2.glo_30m.t00z." +formatutc+ r".grib.grib2")
dlWW3data = str(downloadfolder + r"\multi_2.glo_30m.t00z." +formatlocal+ r".grib.grib2")
outWW3 = open(dlWW3data, 'wb')

print ("Model Date (UTC)")
#print (formatutc)
print (formatlocal)

arcpy.AddMessage("Data Date")
#arcpy.AddMessage(formatutc)
arcpy.AddMessage(formatlocal)

#Combine Strings to form URL
#dlWW3 = str(urlNWW31 + formatutc + urlNWW32)
dlWW3 = str(urlNWW31 + formatlocal + urlNWW32)
print (dlWW3)
arcpy.AddMessage(dlWW3)

urllib.request.urlretrieve(dlWW3,dlWW3data)

arcpy.AddMessage("Retrieved Data from source")


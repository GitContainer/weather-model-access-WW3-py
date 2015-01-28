#-------------------------------------------------------------------------------
# Name:  Retrieve WW3 Model Data from NOAA NOMADS
# Purpose: Downloads a Grib file From NOAA NOMADS
# Author:      John Fry
#               DC Technology Office, Defense Team
# Created:     12/30/2014
# Copyright:   (c) john6807 2014
# Licence:     <your licence>
# Updated 1/25/15 for multi-grid changes in NOAA's website.
# Updated 1/28/15 found smaller dataset to link to
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
# Original URL urlNWW3 = "http://nomads.ncep.noaa.gov/pub/data/nccf/com/wave/prod/multi_1.20150128/nww3.t00z.grib.grib2"
# Going to Parse URL string to allow for the date to be inserted

urlNWW31 = "http://nomads.ncep.noaa.gov/pub/data/nccf/com/wave/prod/multi_1."
urlNWW32= "/nww3.t00z.grib.grib2"

#Get Date/Time- was developed for UTC but found issues on early monring East Coast USA time where model for the day was not yet avail."
# Writing to get local time of machine

#utctime = str(datetime.datetime.utcnow())
localtime = str(datetime.datetime.now())

#formatutc = time.strftime('%Y%m%d',time.strptime(utctime,"%Y-%m-%d %H:%M:%S.%f"))
formatlocal = time.strftime('%Y%m%d',time.strptime(localtime,"%Y-%m-%d %H:%M:%S.%f"))

#dlWW3data = str(downloadfolder + r"\multi_2.glo_30m.t00z." +formatutc+ r".grib.grib2")
dlWW3data = str(downloadfolder + r"\nww3.t00z." +formatlocal+ r".grib.grib2")
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


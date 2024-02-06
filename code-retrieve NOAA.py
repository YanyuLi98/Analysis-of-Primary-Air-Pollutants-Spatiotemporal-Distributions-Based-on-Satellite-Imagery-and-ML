import os
import csv

dir = r"E:/China Meteorological Data/wait/"
# isd

headline = ['year','mon','day','hour','air_temperature','dew_point_temperature',
            'sea_level_pressure','wind_direction','wind_speed','cloud_cover',
            'precipitation_depth_one_hour','precipitation_depth_six_hour','station']

def transisd2csv(year):
    g = os.walk(dir + "china_isd_lite_%s"%year)
            # Iterate over all files in the isd folder for the specified year
    isExists = os.path.exists(dir + "Aggregate%s/" % year)
    if not isExists:
        os.makedirs(dir + "Aggregate%s/" % year)
            # If the year Aggregate folder is not specified, create one
    for path, dir_list, file_list in g:
        for file_name in file_list:
            if file_name!=".DS_Store":
                station = file_name.split("-")[0]
                # Extract the weather station id from each isd file name
                csvFile = open(dir + "Aggregate%s/r%s.csv" % (year, station[:2]), "a", newline='', encoding='utf-8')
                # Name a csv file named after the first two digits of the station id, or create one if not, and store it in the Aggregate folder created earlier
                writer = csv.writer(csvFile)
                writer.writerow(headline)
                f = open(dir + "china_isd_lite_%s/" % year + file_name, "r")
                # Open each file in the isd folder for the specified year one by one
                for line in f:
                    csvRow = line.split()
                    csvRow.append(station)
                    writer.writerow(csvRow)

for year in range(2015,2017):
    transisd2csv(year)
    print("Year %s completed"%year)


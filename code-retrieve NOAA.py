import os
import csv

dir = r"E:/李炎钰/科研/中国气象数据/wait/"
# isd 文件存储路径

headline = ['year','mon','day','hour','air_temperature','dew_point_temperature',
            'sea_level_pressure','wind_direction','wind_speed','cloud_cover',
            'precipitation_depth_one_hour','precipitation_depth_six_hour','station']
# 标题行

def transisd2csv(year):
    g = os.walk(dir + "china_isd_lite_%s"%year)
    # 遍历指定年份isd文件夹内所有文件
    isExists = os.path.exists(dir + "Aggregate%s/" % year)
    if not isExists:
        os.makedirs(dir + "Aggregate%s/" % year)
    # 如果没有指定年份 Aggregate 文件夹，则创建一个
    for path, dir_list, file_list in g:
        for file_name in file_list:
            if file_name!=".DS_Store":
                station = file_name.split("-")[0]
                # 从每个 isd 文件名中提取气象站 id
                csvFile = open(dir + "Aggregate%s/r%s.csv" % (year, station[:2]), "a", newline='', encoding='utf-8')
                # 命名一个以气象站id前两位命名的csv文件，如果没有则创建一个，存储到前面创建的 Aggregate 文件夹中
                writer = csv.writer(csvFile)
                writer.writerow(headline)
                # 写入标题行
                f = open(dir + "china_isd_lite_%s/" % year + file_name, "r")
                # 逐个打开指定年份isd文件夹中的每个文件
                for line in f:
                  	# 对于每个打开的 isd 文件，逐行读取数据
                    csvRow = line.split()
                    # 对于每一行，以空格分割，得到该行数据的 list 形式
                    csvRow.append(station)
                    # 每列末尾加上气象站 id
                    writer.writerow(csvRow)
                    # 向之前创建的 csv 文件里写入每行数据



for year in range(2015,2017):
    transisd2csv(year)
    print("Year %s completed"%year)


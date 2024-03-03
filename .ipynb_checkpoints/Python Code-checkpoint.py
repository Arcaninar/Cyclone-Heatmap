description = ["Not used", "Tropical Depression (TD)", "Tropical Storm (TS)", "Severe Tropical Storm (STS)", "Typhoon (TY)", "Extra-tropical Cyclone (L)" , "Just entering into the responsible area of RSMC Tokyo-Typhoon Center", "Not used", "Tropical Cyclone of TS intensity or higher"]
namelist = []
dflist = []
avglist = []
totallist = []
counttotal = 0
prevyear = 0
maxlat = 0
minlat = 200
maxlong = 0
minlong = 200

with open("bst_all.txt") as f: # f is a file object
    for line in f:
        year = int(line[6:8])
        if prevyear != year and len(namelist) != 0:
            if prevyear < 10:
                filename = 'Storm200' + str(prevyear) + '.xlsx'
            else:
                filename = 'Storm20' + str(prevyear) + '.xlsx'
            
            with pd.ExcelWriter(filename) as writer:
                for i in range(len(namelist)):
                    dflist[i].to_excel(writer, sheet_name=namelist[i])
                    
                dftemp = pd.DataFrame([[namelist[0], avglist[0][0], avglist[0][1], avglist[0][2]]],
                                      index=['one'], columns=['storm code & name', 'average latitude', 'average longitude', 'average wind'])
                for i in range(1, len(avglist)):
                    dftemp1 = pd.DataFrame([[namelist[i], avglist[i][0], avglist[i][1], avglist[i][2]]],
                                          index=['one'], columns=['storm code & name', 'average latitude', 'average longitude', 'average wind'])
                    dftemp = pd.concat([dftemp, dftemp1], ignore_index = True)
                dftemp.to_excel(writer, sheet_name='average data')
            
            namelist = []
            dflist = []
            avglist = []
            totallist.append(counttotal)
            counttotal = 0
            prevyear = year
        
        skip = False
        if year > 24:
            skip = True
        
        numLine = int(line[12:15])
        
        if skip:
            for i in range(numLine):
                next(f)
            continue
        else:
            avglat = 0
            avglong = 0
            avgwind = 0
            counter = 0
            first = True
            prevyear = year
            for i in range(numLine):
                newLine = f.readline()
                wind = int(newLine[33:36])
                
                if wind == 0:
                    continue
                    
                date = int(newLine[0:6])
                time = int(newLine[6:8])
                
                grade = int(newLine[13:14])
                lat = int(newLine[15:18])/10
                long = int(newLine[19:23])/10
                
                pressure = int(newLine[24:28])
                
                avglat += lat
                avglong += long
                avgwind += wind
                counter += 1
                
                if maxlat < lat:
                    maxlat = lat
                if minlat > lat:
                    minlat = lat
                if maxlong < long:
                    maxlong = long
                if minlong > long:
                    minlong = long
                
                if first:
                    df = pd.DataFrame([[date, time, str(grade) + " - " + description[grade], lat, long, pressure, wind]],
                                      index=['one'], columns=['date', 'time', 'description', 'lattitude (degree)', 'longitude (degree)', 'pressure (hPa)', 'wind speed (knot)'])
                    first = False
                else:
                    df1 = pd.DataFrame([[date, time, str(grade) + " - " + description[grade], lat, long, pressure, wind]],
                                      columns=['date', 'time', 'description', 'lattitude (degree)', 'longitude (degree)', 'pressure (hPa)', 'wind speed (knot)'])
                    df = pd.concat([df, df1], ignore_index = True)
            
        avglat = round(avglat/counter, 2)
        avglong = round(avglong/counter, 2)
        avgwind = round(avgwind/counter, 2)
                    
        numberID = line[6:10]
        name = line[29:50]
        name = name.strip()
        
        sname = numberID + ' - ' + name
        
        namelist.append(sname)
        dflist.append(df)
        avglist.append([avglat, avglong, avgwind])
        counttotal += 1

if len(namelist) != 0:
    if year < 10:
        filename = 'Storm200' + str(year) + '.xlsx'
    else:
        filename = 'Storm20' + str(year) + '.xlsx'
    
    with pd.ExcelWriter(filename) as writer:
        for i in range(len(namelist)):
            dflist[i].to_excel(writer, sheet_name=namelist[i])

        dftemp = pd.DataFrame([[namelist[0], avglist[0][0], avglist[0][1], avglist[0][2]]],
                              index=['one'], columns=['storm code & name', 'average latitude', 'average longitude', 'average wind'])
        for i in range(1, len(avglist)):
            dftemp1 = pd.DataFrame([[namelist[i], avglist[i][0], avglist[i][1], avglist[i][2]]],
                                  index=['one'], columns=['storm code & name', 'average latitude', 'average longitude', 'average wind'])
            dftemp = pd.concat([dftemp, dftemp1], ignore_index = True)
        dftemp.to_excel(writer, sheet_name='average data')
    
    totallist.append(counttotal)
        
print(totallist, maxlat, minlat, maxlong, minlong)
year = 2000
df = pd.DataFrame([[year, totallist[0]]],
                  index=['one'], columns=['Year', 'Total Storm'])
for i in range(1, len(totallist)):
    dftemp = pd.DataFrame([[year+i, totallist[i]]],
                          columns=['Year', 'Total Storm'])
    df = pd.concat([df, dftemp], ignore_index = True)

with pd.ExcelWriter("StormOverallStats.xlsx") as writer:
    df.to_excel(writer, sheet_name='overall data')
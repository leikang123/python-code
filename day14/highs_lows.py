import csv
from datetime import datetime
from matplotlib import pyplot as l
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
     reader = csv.reader(f)
     header_row =next(reader)
     #
     dates,highs=[],[]
     #highs = []
     for row in reader:
         cd = datetime.strptime(row[0],"%Y-%m-%d")
         dates.append(cd)
         high =int(row[1])
         highs.append(high)

     print(highs)

     fig = l.figure(dpi=128,figsize=(10,6))
     l.plot(dates,highs,c='red')
     l.title("daily temp,july 2014",fontsize=24)
     l.xlabel('time',fontsize=16)
     fig.autofmt_xdate()
     l.ylabel('temp(F)',fontsize=16)
     l.tick_params(axis='both',which='major',labelsize=16)
     l.show()

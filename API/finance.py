key='API_KEY4f2hPjnXohmK9Yonnm1MIVn9RX7a2cqOJTqNv5Ir89qe7'
symbol=[]
data=list()
exportData=[]
import requests
from datetime import datetime
i=0
try:
    with open('symbol.txt','r') as file:
        for line in file:
            line=line.strip()
            symbol.append(line)
    for i in range(len(symbol)):
        url='https://api.finage.co.uk/last/stock/{}?apikey={}'.format(symbol[i],key)
        data = requests.get(url).json()
        conv=(float(data['timestamp']))/1000
        tims=datetime.fromtimestamp(conv)
    #print(str(tims)[:-7],data['symbol'],data['ask'])
        exportData.append((str(tims)[:-7],data['symbol'],data['ask']))
    with open ('exportData.txt','w') as file:
        for i in range(len(exportData)):
            file.write(str(exportData[i]))
            file.write('\n')
        file.close()
except KeyError:
    print('Exception detected')

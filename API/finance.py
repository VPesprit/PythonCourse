key='API_KEY4f2hPjnXohmK9Yonnm1MIVn9RX7a2cqOJTqNv5Ir89qe7'
symbol=[]
data=list()
import requests
i=0
with open('symbol.txt','r') as file:
    for line in file:
        line=line.strip()
        symbol.append(line)
url='https://api.finage.co.uk/last/stock/{}?apikey={}'.format(symbol[2],key)
data = requests.get(url).json()
print(data['symbol'])


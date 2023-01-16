#https://github.com/public-apis/public-apis

import requests

url = 'https://randomfox.ca/floof/'

data = requests.get(url).json()


#print(data.status_code)
print(data['image'])

import shutil
url = data['image']
data = requests.get(url, stream = True)
with open('fox.jpg','wb') as picture:
        shutil.copyfileobj(data.raw, picture)
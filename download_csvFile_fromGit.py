import pandas as pd
import requests
url = 'https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv'
res = requests.get(url, allow_redirects=True)
with open('MetObjects.csv','wb') as file:
    file.write(res.content)
sales_team = pd.read_csv('MetObjects.csv')
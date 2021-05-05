import requests
import json
import datetime


"https://data.mixpanel.com/api/2.0/export?from_date=" +str('')+ "$to_date=" +str('')
# export data from mixpanel
url = "https://data.mixpanel.com/api/2.0/export?from_date=" +str('')+ "$to_date=" +str('')

headers = {"Authorization": "Basic MDE5ZmI3ZjE1YmFjMjkwZjcxOWZmNDRkOGVlYTJhZjU6"}
response = requests.request("GET", url, headers=headers,stream=True)
#print(response.content)
with open('export_04-05_05-05.json', 'wb') as f:
      for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                  f.write(chunk)







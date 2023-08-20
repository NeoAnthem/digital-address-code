import requests
import json
parameters = {
    # 'address' : '19.108914019118583, 72.86535472954193'
    'address' : '19.1067657, 72.8639412'
}
response = requests.get("https://plus.codes/api", params=parameters)
r = json.loads(response.text)
print(r['plus_code']['global_code'])

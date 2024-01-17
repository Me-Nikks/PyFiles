import requests
import json

url = "https://gbfs.citibikenyc.com/gbfs/2.3/gbfs.json"  
try:
    response = requests.get(url)
    if response.status_code == 200:
       
        data = response.json()
        
        
        print("Decoded Data:", data)
    else:
        print("Failed to fetch data. Status code:", response.status_code)
except requests.RequestException as e:
    print("Request error:", e)

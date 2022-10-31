import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'downloads')

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOAD_DIR, '1.jpg')
url = "https://cdn.britannica.com/97/158797-050-ABECB32F/North-Cascades-National-Park-Lake-Ann-park.jpg"

r = requests.get(url, stream=True)
r.raise_for_status()
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)

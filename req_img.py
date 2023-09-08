import requests
from PIL import Image
from io import BytesIO

image_url = 'https://example.com/image.jpg'
response = requests.get(image_url)

if response.status_code == 200:
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    image.show()
else:
    print("Failed to download the image.")

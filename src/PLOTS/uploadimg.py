import requests
import os
from dotenv import load_dotenv
import requests
import base64


def plots_urls():

    load_dotenv()

    files_to_upload = ['categories', 'markets', 'request_type', 'model_type', 'top_models', 'top_clients']

    urls = []

    print('Uploading ploted images...')

    for file in files_to_upload:

        with open(f'./PLOTS/img/{file}.jpg', 'rb') as img:
            img_encoded = base64.b64encode(img.read())

        data = {
        'image':img_encoded
        }

        api_key = os.environ.get('IMGBB_KEY')
        resp = requests.post(f'https://api.imgbb.com/1/upload?key={api_key}', data=data)
        response_data = resp.json()
        url = response_data
        urls.append(url['data']['url'])
    
    print('Uploaded!!')
    return urls
    


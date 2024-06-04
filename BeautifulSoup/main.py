import requests
def Saver(url, path):
    response = requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(response.text)
url = 'https://analyticsindiamag.com/india-is-likely-to-develop-its-foundational-model-this-year/'
Saver(url, 'Data/aim.html')

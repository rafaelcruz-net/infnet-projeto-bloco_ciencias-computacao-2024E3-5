import requests
import time

api_key = '1848e3df-af48-4c59-84ea-7bcfd43430d3'
urls = [
    "https://xpto.com.br",
    "https://oglobo.globo.com/"
    "https://secure-site.com"
]

headers = {'API-key': api_key}

def scan_url(url):
    data = {"url": url, "visibility": "public"}
    response = requests.post("https://urlscan.io/api/v1/scan", headers=headers, json=data)
    if (response.status_code == 200):
        result = response.json()
        print(f"URL {url} analisada com sucesso, Resultado: {result['result']}")
    else:
        print(f"Erro ao analisar a url {url}")

for url in urls:
    scan_url(url)
    time.sleep(5)
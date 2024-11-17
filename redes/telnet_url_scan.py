import telnetlib
import requests


def fetch_urls_from_router(host, username, password):
    try:
        telnet = telnetlib.Telnet(host)
        telnet.read_until(b'Username: ')
        telnet.write(username.encode() + b'\n')

        telnet.read_until(b'Password: ')
        telnet.write(password.encode() + b'\n')

        telnet.write(b'show suspicious-urls\n')
        telnet.write(b'exit\n')

        output = telnet.read_all().decode("ascii")

        return [line.strip() for line in output.splitlines() if 'http' in line]
    except Exception as e:
        print(f"erro ao coletar urls do roteador, {e}")
        return []

def analyze_urls(urls):
    api_key = '1848e3df-af48-4c59-84ea-7bcfd43430d3'
    headers = {'API-key': api_key}
    for url in urls:
        data = {"url": url, "visibility": "public"}
        response = requests.post("https://urlscan.io/api/v1/scan", headers=headers, json=data)
        if (response.status_code == 200):
            result = response.json()
            print(f"URL {url} analisada com sucesso, Resultado: {result['result']}")
        else:
            print(f"Erro ao analisar a url {url}")

urls = fetch_urls_from_router("192.168.0.1", "admin", "password")
analyze_urls(urls)

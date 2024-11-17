import telnetlib

def check_port(host, port):
    try:
        telnet = telnetlib.Telnet(host, port, timeout=5)
        print(f'Porta {port} em {host} está aberta')
        telnet.close()
    except Exception:
        print(f'Porta {port} em {host} não está aberta')


host = '127.0.0.1'
ports = [23, 22, 80, 443, 3306]

for port in ports:
    check_port(host, port)
    
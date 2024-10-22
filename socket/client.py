import socket

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', int(input("Digite a porta do servidor"))))
    s.sendall(input('Digite a mensagem: ').encode('utf-8'))
    data = s.recv(1024)
    print(f'Recebido pelo servidor : {data.decode()}')
    s.close()

if (__name__ == "__main__"):
    client()
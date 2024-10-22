import socket

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", int(input("Digite a porta que deseja subir o servidor"))))
    s.listen(1)
    conn, addr = s.accept()
    print(f'Conexão estabelecida com o {addr}')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f'Mensagem recebida: {data.decode()}')
        conn.sendall(data)
    conn.close()

if (__name__ == "__main__"):
    server()
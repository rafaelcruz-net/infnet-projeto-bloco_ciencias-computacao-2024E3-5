import socket
import threading

clientes = []

def handle_client(conn, addr):
    print(f'Nova conexão: {addr}')
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f'{addr}: {msg}')

            #Reencaminhar as mensagem para todos os cliente que estão conectados
            broadcast(msg, conn)
        except:
            clientes.remove(conn)
            conn.close()
            break

#Envia a mensagem para todos os clientes conectados
def broadcast(msg, conn):
    for client in clientes:
        if (client != conn):
            try:
                client.send(msg.encode())
            except:
                client.close()
                clientes.remove(client)

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 4042))
    s.listen()
    print('Servidor aguardando conexões')

    while True:
        conn, addr = s.accept()
        clientes.append(conn) # Adiciona a nova conexão a lista de clientes
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #Não bloqueia a execução do server
        thread.start()

if (__name__ == "__main__"):
    server()
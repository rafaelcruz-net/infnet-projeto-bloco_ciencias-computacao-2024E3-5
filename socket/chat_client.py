import socket
import threading

#função que recebe mensagens do servidor

def receive_messages(server):
    while True:
        try:
            msg = server.recv(1024).decode()
            print(f"Mensagem: {msg} \n")
        except:
            print('Erro ao receber a mensagem')
            server.close()
            break


def client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 4042))

    #Cria uma thread para receber as mensagens do servidor
    thread = threading.Thread(target=receive_messages, args=(c,))
    thread.start()

    #Envia a mensagens do servidor
    while True:
        msg = input('Escreva a mensagem: \n')
        if (msg.lower() == "sair"):
            break
        c.send(msg.encode()) # Envia a mensagem para o servidor
    c.close()

if (__name__ == "__main__"):
    client()
        
    



import socket, threading

class Server:
    def __init__(self, ipaddr, port):
        self.IP   = ipaddr
        self.PORT = port

        self.clients = []
        
        while True:
            try:    
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.bind((self.IP, self.PORT))
                break
            except:
                print('Error to start the server')
        
        self.accept_connections()


    def accept_connections(self):
        self.sock.listen(100)

        while True:
                new_client = self.sock.accept()
                self.clients.append(new_client)

                print("new connection from", new_client[1])

                threading.Thread(target=self.handle_client, args=[new_client[0]]).start()
        
    def handle_client(self, client):
        while True:
            try:
                data = client.recv(1024)
                self.handle_data(client, data)
            except socket.error:
                print("closing connection with client")
                client.close()
                break

    # possibly abstract method
    def handle_data(self, client, data):
        for i in self.clients:
            # if client != i[0]:
            i[0].sendall(data)


def main():
    server = Server('', 8080)


if __name__ == "__main__":
    main()
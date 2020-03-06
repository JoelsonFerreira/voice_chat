import socket, threading

class Client:
    def __init__(self, ipaddr, port):
        self.IP   = ipaddr
        self.PORT = port
        
        while True:
            try:    
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.IP, self.PORT))
                break
            except:
                print('Error to connect the server')
        
        threading.Thread(target=self.recv).start()
        
    def send(self, data):
        self.sock.sendall(data)

    def recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                
                self.handle_data(data)

            except socket.error:
                self.sock.close()
                break

    # possibly abstract method
    def handle_data(self, data):
        pass

    def close(self):
        self.sock.close()

import socketserver

class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("New client Connected",self.client_address)
        data = "predefined value"
        while len(data):
            data = self.request.recv(2048)
            print("new message has been received from: ", self.client_address)
            self.request.send(b""" We have received your message: "%s" """ %data)



serverAddr = ("localhost", 773)
server = socketserver.TCPServer(serverAddr, ClientHandler)
server.serve_forever()

















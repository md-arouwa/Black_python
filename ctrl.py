

def handle(self,client_socket,user):
    if self.args.execute:
        output=execute(self.args.execute)
        self.client_socket.send(output.encode())
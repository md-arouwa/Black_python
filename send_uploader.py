


def send(self):
    self.socket.connect((self.args.target,self.args.port))
    if self.buffer:
        self.socket.send(self.buffer)

    try:
        while True:
            recv_len=1
            response=''
            while recv_len:
                data=self.socket.recv(4096)
                recv_len=len(data)
                response+=data.decode()
                if recv_len < 4096:
                    break
            if response:
                print(response)
                buffer=''
                buffer+='\n'
                self.socket.send(buffer.encode())
    except KeyboardInterrupt:
        print('User tarminated')
        self.socket.close()
        sys.exit()
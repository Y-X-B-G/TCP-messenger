import socket
BUFFER_SIZE: int = 1000

HOST: str = 'localhost' #Change the ip address as needed
PORT: int = 1234

def main() -> None:
    with socket.create_connection((HOST, PORT), source_address=None, all_errors=False) as s:
        print(s.recv(BUFFER_SIZE).decode())
        while(True):
            value = input("Enter message or 'exit' to disconnect or 'status' to see history or list to get list of files to download: ")
            if (value == "exit"):
                break
            elif (value == "list"):
                s.send(value.encode())
                data: bytes = s.recv(BUFFER_SIZE).decode()
                print(data)
                file_name: str = input("Enter file name: ")
                s.send(file_name.encode())
                data: bytes = s.recv(BUFFER_SIZE)
                #the messages were not getting through so we should wait for 1 second
                if (data.decode() == "That file is not in the directory"):
                    print(data)
                    pass
                else:
                    filename_create = file_name
                    with open(filename_create, 'wb') as f:
                        while True:
                            print(data)
                            #f.write(data)
                            if data == b'EOF':
                                break
                            elif b'EOF' in data:
                                eof_index = data.find(b'EOF')
                                f.write(data[:eof_index]) 
                                break
                            else:
                                f.write(data)

                            data = s.recv(BUFFER_SIZE)
            else:
                s.send(value.encode())
                data: bytes = s.recv(BUFFER_SIZE)
                print(data.decode())

if __name__ == "__main__":
    main()
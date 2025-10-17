import socket

BUFFER_SIZE: int = 100000

HOST: str = 'localhost' #Change the ip address as needed
PORT: int = 1234

def main() -> None:
    with socket.create_connection((HOST, PORT), source_address=None, all_errors=False) as s:
        file_num: int = 0
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
                data: bytes = s.recv(BUFFER_SIZE).decode()
                if (data == "That file is not in the directory"):
                    print(data)
                    pass
                else:
                    filename_create = file_name+str(file_num)+'.txt'
                    file_num += 1
                    fo = open(filename_create, "w")
                    while data:
                        if not data:
                            break
                        else:
                            fo.write(data)
                            data = s.recv(BUFFER_SIZE).decode()
                    fo.close()
            else:
                s.send(value.encode())
                data: bytes = s.recv(BUFFER_SIZE)
                print(data.decode())

if __name__ == "__main__":
    main()
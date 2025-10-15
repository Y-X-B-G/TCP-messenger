import socket

BUFFER_SIZE: int = 1000

HOST: str = 'localhost' #Change the ip address as needed
PORT: int = 1234

def main() -> None:
    with socket.create_connection((HOST, PORT), source_address=None, all_errors=False) as s:
        while(True):
            value = input("Enter message or 'BREAK' to disconnect: ")
            if (value == "BREAK"):
                break
            else:
                s.send(value.encode())
                data: bytes = s.recv(BUFFER_SIZE)
                print(data.decode())
if __name__ == "__main__":
    main()
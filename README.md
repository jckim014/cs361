# Password Microservice

This microservice is powered by Python sockets to receive generic socket requests and will return a randomly generated password string.
The microservice will return that password string through a Python socket.

### How to request:
Write/build a Python socket client to send a generic request to the server (content doesn't matter, any request will suffice).

### Example Call:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(b"Requesting password")
    password = s.recv(1024).decode('utf-8')

### How to receive:
A message in string format will be returned from the socket server. The above code demonstrates how to receive the request - the password variable is a string.

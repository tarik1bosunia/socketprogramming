import socket
import ssl
import base64

# Gmail SMTP server details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # SSL port

# Email login credentials
USERNAME = "bosuniamdtarik005@gmail.com"  # Replace with your Gmail address
PASSWORD = "ilassxeqjfpiaagjkf"         # Replace with your Gmail password or app-specific password

# Email details
from_email = "tata@gmail.com"
to_email = "codewithtata@gmail.com"
subject = "Test Email from Python Socket"
body = "This is a test email sent using socket programming in Python."

# Compose the email content
message = f"From: {from_email}\r\nTo: {to_email}\r\nSubject: {subject}\r\n\r\n{body}"

try:
    # Create a socket and wrap it in SSL for secure connection
    context = ssl.create_default_context()
    with socket.create_connection((SMTP_SERVER, SMTP_PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=SMTP_SERVER) as ssock:
            print("Connected to the Gmail SMTP server.")

            # Read server response
            ssock.recv(1024)

            # Send EHLO command to the server
            ssock.send(b"EHLO gmail.com\r\n")
            print(ssock.recv(1024).decode())

            # Authenticate with the server using Base64 encoding
            ssock.send(b"AUTH LOGIN\r\n")
            print(ssock.recv(1024).decode())

            # Send username and password in Base64 encoding
            ssock.send(base64.b64encode(USERNAME.encode()) + b"\r\n")
            print(ssock.recv(1024).decode())

            ssock.send(base64.b64encode(PASSWORD.encode()) + b"\r\n")
            auth_response = ssock.recv(1024).decode()
            print(auth_response)
            if "235" not in auth_response:
                raise Exception("Authentication failed")

            # Send the MAIL FROM command
            ssock.send(f"MAIL FROM:<{from_email}>\r\n".encode())
            print(ssock.recv(1024).decode())

            # Send the RCPT TO command
            ssock.send(f"RCPT TO:<{to_email}>\r\n".encode())
            print(ssock.recv(1024).decode())

            # Send the DATA command to indicate the start of the message body
            ssock.send(b"DATA\r\n")
            print(ssock.recv(1024).decode())

            # Send the email content and end with a single period on a new line
            ssock.send((message + "\r\n.\r\n").encode())
            print(ssock.recv(1024).decode())

            # Close the SMTP session with the QUIT command
            ssock.send(b"QUIT\r\n")
            print(ssock.recv(1024).decode())

except Exception as e:
    print("Failed to send email:", e)

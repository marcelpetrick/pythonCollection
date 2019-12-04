# taken from: https://wiki.python.org/moin/TcpCommunication
# working

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 6123
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_STREAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.listen(1)

# main
conn, addr = sock.accept()
print('Connection address:', addr)
while 1:
    print("before receive")
    data = conn.recv(BUFFER_SIZE)
    print("after receive")

    if not data:
        break
    print("received data:", data)
    #conn.send(data)  # echo

conn.close()

# --------------------------------------------------------------------
# C:\Users\mpe\Desktop\MarcelsFolder\coding\pythonCollection\venv1\Scripts\python.exe C:/Users/mpe/Desktop/MarcelsFolder/coding/pythonCollection/UdpReceiver/TcpReceiver.py
# Connection address: ('127.0.0.1', 56265)
# before receive
# after receive
# received data: b'testPacket'
# before receive
# after receive
#
# Process finished with exit code 0

import socket
import json


sock = socket.socket()
sock.bind(('', 15010))
sock.listen(1)
conn, addr = sock.accept()
data_ = conn.recv(1024)
data_l = data_.decode('utf-8')
print(data_)

conn.close()


def decoders(json_data):
    ret_data = json.loads(json_data)
    return ret_data


print(decoders(data_l))


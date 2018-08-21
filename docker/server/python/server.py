from datetime import datetime
import socket

#address = ('localhost', 5000)
address = ('192.168.29.164', 5555)
# address = ('10.0.1.52', 5555)
max_size = 1000

print('Starting the server at', datetime.now())
print('Waiting for a client to call. at ', address)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

try:
    while True:
        client, addr = server.accept()
        data = client.recv(max_size)

        print('At', datetime.now(), client, 'said', data)
        if data == b'500000FE03FF00000006001004010000':
            # サブヘッダ
            data = 'D000'
            # アクセス経路
            data += '00FF03FF00'
            # データ長(16進数)
            data += '0044'
            # 終了コード
            data += '0000'
            # 応答データ
            data += 'measured data'
            client.sendall(data.encode("UTF-8"))
        else:
            client.sendall(b'invailed data')
        client.close()
except KeyboardInterrupt:
    print("server closing")
    client.close()
    server.close()
    print("server closed")

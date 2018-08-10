# coding: utf-8
import socket

target_host = "127.0.0.1"
target_port = 6666

# ソケットオブジェクトの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# サーバーへ接続
client.connect((target_host, target_port))

# データの送信
client.send(b"ABCDEF")

# データの受信
response = client.recv(4096)

print(response)
# -*- coding:utf-8 -*-
import socket
from datetime import datetime
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Client:
    def __init__(self, url, port, max_size):
        self.address = (url, port)
        self.max_size = max_size

    def send_request(self, cmd):
        print('Starting the client at', datetime.now())
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect(self.address)
            print("connected")
        except socket.gaierror as e:
            print(type(e))
            print(e)
        # client.send(b"from nadechin")
        client.sendall(cmd.encode("UTF-8"))

        data = client.recv(self.max_size)
        print('At', datetime.now(), 'get replied data = ', data)
        client.close()

if __name__ == "__main__":
    client = Client('localhost', 5000, 1000)

    # 3Eフレーム　ASCIIコード
    cmd = ''
    # サブヘッダ
    cmd += '5000'
    # アクセス経路(接続局(直接つなぐ場合は0),ネットワーク番号(0),PC番号(FE),要求先ユニットI/O番号(03FFH),要求先ユニット局番号(00),自局番号(00))
    cmd += '00FE03FF0000'
    # 要求データ長（監視タイマ+要求データのバイト数を16進数）
    cmd += '0006'
    # 監視タイマ（待ち時間4秒(単位: 250ms)）
    cmd += '0010'
    # 要求データ(ex)ワード単位の一括読出しは0401サブコマンド0000)
    cmd += '04010000'

    client.send_request(cmd)
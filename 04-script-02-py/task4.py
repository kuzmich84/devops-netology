#!/usr/bin/env python3
import socket
import os

urlServices = ["drive.google.com", "mail.google.com", "google.com"]
fileName = 'urlList.txt'

if os.stat(fileName).st_size != 0:
    f = open(fileName, "r")
    lines = f.readlines()
    urlList = [line[:-1] for line in lines]
    currentList = []
    for i in range(len(urlServices)):
        if urlList[i] == socket.gethostbyname(urlServices[i]):
            currentList.append(socket.gethostbyname(urlServices[i]))
            print(f"{urlServices[i]} - {socket.gethostbyname(urlServices[i])}")
        else:
            currentList.append(socket.gethostbyname(urlServices[i]))
            print(f"[ERROR] {urlServices[i]} IP mismatch: {urlList[i]} {socket.gethostbyname(urlServices[i])}")
    f.close()
    f = open(fileName, 'w')
    for i in currentList:
        f.write(i)
        f.write("\n")
    f.close()
else:
    f = open(fileName, 'w')
    for url in urlServices:
        nameHost = socket.gethostbyname(url)
        f.write(nameHost)
        f.write("\n")
    f.close()

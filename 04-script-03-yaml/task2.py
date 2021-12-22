#!/usr/bin/env python3
import json
import socket
import os
import subprocess

import yaml

urlServices = ["drive.google.com", "mail.google.com", "google.com"]
fileName = 'urlList.txt'


def create_file(url_list):
    f = open(fileName, 'w')
    for url in url_list:
        name_host = socket.gethostbyname(url)
        f.write(name_host)
        f.write("\n")
    f.close()


if os.path.isfile(fileName):
    if os.stat(fileName).st_size != 0:
        f = open(fileName, "r")
        lines = f.readlines()
        urlList = [line[:-1] for line in lines]
        currentList = []
        d = []
        for i in range(len(urlServices)):
            if urlList[i] == socket.gethostbyname(urlServices[i]):
                currentList.append(socket.gethostbyname(urlServices[i]))
                d.append({urlServices[i]: socket.gethostbyname(urlServices[i])})
                print(f"{urlServices[i]} - {socket.gethostbyname(urlServices[i])}")
            else:
                currentList.append(socket.gethostbyname(urlServices[i]))
                d.append({urlServices[i]: socket.gethostbyname(urlServices[i])})
                print(f"[ERROR] {urlServices[i]} IP mismatch: {urlList[i]} {socket.gethostbyname(urlServices[i])}")
        f.close()
        with open("urlList.json", 'w') as write_file:
            json.dump(d, write_file, indent=4)
        with open("urlList.yml", 'w') as write_file:
            yaml.dump(d, write_file,
                      indent=4,
                      sort_keys=False,
                      default_flow_style=False,
                      explicit_start=True,
                      explicit_end=True
                      )

        f = open(fileName, 'w')
        for i in currentList:
            f.write(i)
            f.write("\n")
        f.close()
    else:
        create_file(urlServices)
else:
    create_file(urlServices)
    subprocess.Popen(['python3', 'task2.py'])

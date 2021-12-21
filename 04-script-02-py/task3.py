#!/usr/bin/env python3
import sys
import os

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()

bash_command = ["cd " + path, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(path + prepare_result)

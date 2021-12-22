### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-03-yaml/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
Исправленный JSON: 
```json
{
  "info": "Sample JSON output from our service\t",
  "elements": [
    {
      "name": "first",
      "type": "server",
      "ip": 7175
    },
    {
      "name": "second",
      "type": "proxy",
      "ip": "71.78.22.43"
    }
  ]
}
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
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
```

### Вывод скрипта при запуске при тестировании:
```
dmitry@dmitry-N56VZ:~/PycharmProjects/devops-netology/04-script-03-yaml$ ./task2.py
drive.google.com - 74.125.205.194
[ERROR] mail.google.com IP mismatch: 173.194.222.19 142.251.1.18
[ERROR] google.com IP mismatch: 108.177.14.102 173.194.221.138

```

### json-файл(ы), который(е) записал ваш скрипт:
```json
[
    {
        "drive.google.com": "74.125.205.194"
    },
    {
        "mail.google.com": "142.251.1.18"
    },
    {
        "google.com": "173.194.221.138"
    }
]
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
---
-   drive.google.com: 74.125.205.194
-   mail.google.com: 142.251.1.18
-   google.com: 173.194.221.138
...
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

### Ваш скрипт:
```python
???
```

### Пример работы скрипта:
???

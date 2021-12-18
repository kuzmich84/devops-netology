#!/usr/bin/env bash
hosts=(192.168.0.1 173.194.222.113 87.250.250.242)
port=80
connected=доступен
disconnected=недоступен
for i in "${hosts[@]}"
do
  for j in {1..5}
  do
   curl  -s -m 2 "$i":"$port" >/dev/null
    if(($? == 0))
    then
      echo "$(date)" - "$i" - $connected >> hosts.log
    else
      echo "$(date)" - "$i" -$disconnected >> hosts.log
    fi
    if(($? != 0))
    then
      break
    fi
  done
done
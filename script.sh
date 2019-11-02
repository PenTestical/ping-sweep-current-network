#!/bin/bash

#scans current network with a for loop

for i in {1..254}; do
   if output=$(ping -c 1 192.168.1.$i); then
   echo "$output" | grep "^---" | cut -f2 -d ' '
fi
done

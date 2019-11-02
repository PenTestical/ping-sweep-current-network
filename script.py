#!/usr/bin/python

import multiprocessing
import os
import sys
import subprocess

nrange = "192.168.1."

for i in range(1, 254):
    address = nrange + str(i)
    final = subprocess.call(['fping','-a', '-q', address])

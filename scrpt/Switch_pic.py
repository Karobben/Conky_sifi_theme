#!/usr/bin/env python3
import sys
import os,time

PATH = sys.path[0] +"/../Nature/"
Num = time.strftime("%M")

List = os.listdir(PATH)
List.sort()
List = List[1:]
CMD = "cp "+PATH + List[int(Num) % int(len(List)-1)]+" "+PATH+"000.png"
os.system(CMD)

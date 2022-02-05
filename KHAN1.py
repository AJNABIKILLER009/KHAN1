# -*- coding: utf-8

# author by SUBHAN KHAN

import os

try:

	os.system("pip2 install requests")

	import bs4

except ImportError:

	os.system("pip2 install bs4")

import os, sys, re, time, requests, json, random, calendar

from multiprocessing.pool import ThreadPool

from bs4 import BeautifulSoup as parser

from datetime import datetime

from datetime import date

loop = 0

id = []

ok = []

cp = []

ct = datetime.now()

n = ct.month

bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

def  jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(000.05)

my_date = date.today()

hr = calendar.day_name[my_date.weekday()]

tBilall = ("%s-%s-%s-%s"%(hr, ha, op, ta))

tgl = ("%s %s %s"%(ha, op, ta))

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

def logo():

	os.system("clear")

	print("""\x1b[0;32m

\x1b[0;31m▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄      

\x1b[0;32m▐░░▌     ▐░░▌▐░░░░░░░░░░░▌     

\x1b[0;33m▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌     

\x1b[0;34m▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌     

\x1b[0;35m▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌     

\x

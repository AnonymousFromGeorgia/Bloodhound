#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
os.system('clear')

import subprocess

import signal

def keyboardInterruptHandler(signal, frame):
    print("\nპროგრამა გაითიშა.".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("სია.txt","r");
	link = raw_input("შეიყვანეთ სასურველი ვებსაიტის ბმული \n(მაგ: nimushi.ge ან www.nimushi.com): ")
	
	print "\nმიმდინარეობს " + link + "-ის სკანირება...\n"
	
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	print("           __     ")
	print("      (___()'`;   ")
	print("      /,    /`    ")
	print("     // ''--\     ")
	print("   Bloodhound.py\n")
	print("▶ Coded by გიო რგი ◀\n")
	print("https://github.com/AnonymousFromGeorgia/Bloodhound\n")
	print("ℹ️უფასო ხელსაწყო საიტებზე Admin Panel-ების მოსაძებნად (Admin Panel Finder)\n")
	print("ℹ️პროგრამის გასათიშად გამოიყენეთ კლავიშების კომბინაცია CTRL+C\n")
	print("ℹ️შეიყვანეთ რეალური ბმული, წინააღმდეგ შემთხვევაში ხელსაწყო არ იმუშავებს\n")

Credit()
findAdmin()

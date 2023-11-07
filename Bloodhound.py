#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import signal
import requests

os.system('clear')

def keyboardInterruptHandler(signal, frame):
    print("\nპროგრამა გაითიშა.")
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

def findAdmin():
    with open("სია.txt", "r") as f:
        link = input("შეიყვანეთ სასურველი ვებსაიტის ბმული \n(მაგ: nimushi.ge ან www.nimushi.com): ")

        print("\nმიმდინარეობს " + link + "-ის სკანირება...\n")

        for sub_link in f:
            sub_link = sub_link.strip()
            req_link = f"https://{link}/{sub_link}"
            try:
                response = requests.get(req_link)
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                continue
            except requests.exceptions.RequestException as e:
                continue
            else:
                print("OK => ", req_link)

def Credit():
    print("           __     ")
    print("      (___()'`;   ")
    print("      /,    /`    ")
    print("     // ''--\     ")
    print("   Bloodhound.py\n")
    print("▶ Coded by გიო რგი ◀\n")
    print("https://github.com/AnonymousFromGeorgia/Bloodhound\n")
    print("> უფასო ხელსაწყო საიტებზე Admin Panel-ების მოსაძებნად (Admin Panel Finder)\n")
    print("> პროგრამის გასათიშად გამოიყენეთ კლავიშების კომბინაცია CTRL+C\n")
    print("> შეიყვანეთ რეალური ბმული, წინააღმდეგ შემთხვევაში ხელსაწყო არ იმუშავებს\n")

Credit()
findAdmin()

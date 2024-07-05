import os, time
from colorama import Fore

blue = Fore.BLUE
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW

#import cod checker
from Modules.cod import checker

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    def check_input():
        options = [1, 2, "1", "2"]
        if op == 'x':
            print(yellow + "[-] Closing...")
            time.sleep(1.5)
            exit()

        if op in options:
            pass
        else:
            print(red + "[!] Invalid Options")
            time.sleep(1.5)
            clear()
            main()

    print(blue + r"""
 ______     ______     _____    
/\  ___\   /\  __ \   /\  __-. Made By ISellStuff  
\ \ \____  \ \ \/\ \  \ \ \/\ \ [Note] These Are Activison Accounts
 \ \_____\  \ \_____\  \ \____- 
  \/_____/   \/_____/   \/____/  
    
    [1] Call Of Duty Account Checker
    [x] Exit                           """)
    
    op = input(blue + "\n> ")
    check_input()

    if op == '1':
        clear()
        checker()

main()

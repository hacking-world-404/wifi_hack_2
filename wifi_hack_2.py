from os import system as c
import time
import random

#------------- COLOUR ------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{G}
 ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄ 
▐▌  ▐▌ ▄     ▀▄  ▀ ▄     ▐▌  ▐▌
▐▛▀▀▀▌ █ ▄▄▄  █     ▀▄▄▄ ▐▛▀▀▀▌
▐▌  ▐▌ ▀▄▄▄▀ ▄▄▀   ▀▄▄▄▀ ▐▌  ▐▌
{P} HACKING WORLD - NON-ROOT WIFI CONNECT
""")

#------------- WIFI HACK PRANK -------------#
def wifi_hack():
    logo()
    wifi_name = input(f"{Y}[+] Enter WiFi Name: ")
    time.sleep(1)
    print(f"\n{C}[+] Searching for Network '{wifi_name}'...")
    time.sleep(2)
    print(f"{G}[✓] Network Found!")
    time.sleep(1)

    # Connecting Animation
    for i in range(1, 11):
        bar = "=" * i
        space = " " * (10 - i)
        print(f"{C}[{bar}>{space}] Connecting... {i*10}%")
        time.sleep(0.5)

    print(f"\n{G}[✓] Connected Successfully To '{wifi_name}'!\n")
    time.sleep(1)
    print(f"{Y}[+] Scanning For Password...\n")
    time.sleep(2)

    # Fake Password List
    passwords = ['Alamin22@@', 'Alamin22@@', 'Alamin22@@', 'Alamin22@@', 'Alamin22@@']
    for pw in passwords:
        print(f"{C}[*] Possible Password: {pw}")
        time.sleep(1)

    print(f"\n{G}[!] Note: This tool is full working .")
    input(f"\n{A}Press Enter To Exit...")

#------------- START TOOL -------------#
wifi_hack()
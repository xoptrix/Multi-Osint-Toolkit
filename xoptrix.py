#!/usr/bin/python3
# ==========================================
#        X O P T R I X   C O D E
#        Multi OSINT Toolkit
# ==========================================

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# COLORS
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
B = '\033[1;34m'
C = '\033[1;36m'
W = '\033[1;37m'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    clear()
    print(f"""{C}
██╗  ██╗ ██████╗ ██████╗ ████████╗██████╗ ██╗██╗  ██╗
╚██╗██╔╝██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝
 ╚███╔╝ ██║   ██║██████╔╝   ██║   ██████╔╝██║ ╚███╔╝
 ██╔██╗ ██║   ██║██╔═══╝    ██║   ██╔══██╗██║ ██╔██╗
██╔╝ ██╗╚██████╔╝██║        ██║   ██║  ██║██║██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
{W}        X O P T R I X  https://t.me/xoptrixx
{Y}------------------------------------------------
{G} Author : Xoptrix
{Y}------------------------------------------------
""")


# ===============================
# IP TRACKER
# ===============================
def ip_tracker():
    banner()
    ip = input(f"{C}Enter Target IP : {G}")
    data = requests.get(f"http://ipwho.is/{ip}").json()

    print(f"\n{Y}========== IP INFORMATION ==========\n")
    print(f"{W}IP Address   : {G}{ip}")
    print(f"{W}Country      : {G}{data['country']}")
    print(f"{W}City         : {G}{data['city']}")
    print(f"{W}Region       : {G}{data['region']}")
    print(f"{W}Latitude     : {G}{data['latitude']}")
    print(f"{W}Longitude    : {G}{data['longitude']}")
    print(f"{W}ISP          : {G}{data['connection']['isp']}")
    print(f"{W}Domain       : {G}{data['connection']['domain']}")
    print(f"{W}ASN          : {G}{data['connection']['asn']}")
    print(f"{W}Google Maps  : {G}https://maps.google.com/?q={data['latitude']},{data['longitude']}")


# ===============================
# SHOW YOUR IP
# ===============================
def my_ip():
    banner()
    ip = requests.get("https://api.ipify.org").text
    print(f"\n{Y}Your Public IP : {G}{ip}\n")


# ===============================
# PHONE NUMBER TRACKER
# ===============================
def phone_tracker():
    banner()

    number = input(f"{C}Enter Phone Number (+country) : {G}")

    parsed = phonenumbers.parse(number)
    region = geocoder.description_for_number(parsed, "en")
    sim = carrier.name_for_number(parsed, "en")
    zone = timezone.time_zones_for_number(parsed)

    print(f"\n{Y}========== PHONE INFO ==========\n")
    print(f"{W}Number        : {G}{number}")
    print(f"{W}Region        : {G}{region}")
    print(f"{W}Carrier       : {G}{sim}")
    print(f"{W}Timezone      : {G}{', '.join(zone)}")
    print(f"{W}Valid Number  : {G}{phonenumbers.is_valid_number(parsed)}")


# ===============================
# USERNAME TRACKER
# ===============================
def username_tracker():
    banner()

    username = input(f"{C}Enter Username : {G}")

    sites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}"
    }

    print(f"\n{Y}========== USERNAME SEARCH ==========\n")

    for site, url in sites.items():
        r = requests.get(url)

        if r.status_code == 200:
            print(f"{G}[FOUND]{W} {site} : {url}")
        else:
            print(f"{R}[NOT FOUND]{W} {site}")


# ===============================
# MENU
# ===============================
def menu():
    banner()

    print(f"""{W}
{C}[01]{W} IP Address Tracker
{C}[02]{W} Show My IP
{C}[03]{W} Phone Number Tracker
{C}[04]{W} Username Tracker
{C}[00]{W} Exit
""")


# ===============================
# MAIN PROGRAM
# ===============================
while True:
    menu()

    choice = input(f"{G}Select Option : {W}")

    if choice == "01":
        ip_tracker()

    elif choice == "02":
        my_ip()

    elif choice == "03":
        phone_tracker()

    elif choice == "04":
        username_tracker()

    elif choice == "00":
        print(f"{R}Exiting Xoptrix Toolkit...")
        break

    else:
        print(f"{R}Invalid Option!")

    input(f"\n{Y}Press Enter to continue...")

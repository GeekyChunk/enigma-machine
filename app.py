#!/bin/env python3

import pickle
from colorama import Fore, Back, Style
from enigma import encode, decode
from helpers import clear

with open("./data/rotors.dat", "rb") as f:
    rotors = pickle.load(f)

def menu():
    clear()
    print(Fore.GREEN + "\t")
    print(Style.BRIGHT + \
          "\t _____ _   _ ___ ____ __  __    _ ")
    print("\t| ____| \ | |_ _/ ___|  \/  |  / \ ")
    print("\t|  _| |  \| || | |  _| |\/| | / _ \ ")
    print("\t| |___| |\  || | |_| | |  | |/ ___ \ ")
    print("\t|_____|_| \_|___\____|_|  |_/_/   \_\ ")
    print()
    print(Fore.WHITE + "\t{1}--Encode")
    print("\t{2}--Decode")
    print("\t{9}--Exit")
    print()

while True:
    try:
        menu()

        prompt = input(Fore.BLUE + Style.BRIGHT + "engima ~# " + Fore.WHITE + Style.NORMAL)

        if not prompt.isdigit():
            continue
        else:
            prompt = int(prompt)

        if prompt == 9:
            print("\nGood Bye :)")
            break

        elif prompt == 1:
            print()
            plain = input(Style.BRIGHT + Back.GREEN + Fore.BLACK + "Enter plain:" + Fore.RESET + Back.RESET + " ")
            print()
            print(Style.BRIGHT + Fore.CYAN + "[*] Encoding '"+ Fore.RED + plain + Fore.CYAN + "'\n")
            cipher = encode(rotors, plain)
            print(Style.BRIGHT + Fore.CYAN + "[*] Cipher is: '"+ Fore.RED + cipher + Fore.CYAN + "'\n")
            input(Style.NORMAL + Fore.LIGHTBLACK_EX + "Press [Enter] to return")

        elif prompt == 2:
            print()
            cipher = input(Style.BRIGHT + Back.GREEN + Fore.BLACK + "Enter cipher:" + Fore.RESET + Back.RESET + " ")
            print()
            print(Style.BRIGHT + Fore.CYAN + "[*] Decoding '"+ Fore.RED + cipher + Fore.CYAN + "'\n")
            plain = decode(rotors, cipher)
            print(Style.BRIGHT + Fore.CYAN + "[*] Plain is: '"+ Fore.RED + plain + Fore.CYAN + "'\n")
            input(Style.NORMAL + Fore.LIGHTBLACK_EX + "Press [Enter] to return")

    except KeyboardInterrupt:
        print("\n\nGood Bye :)")
        break
    except EOFError:
        print("\n\nGood Bye :)")
        break

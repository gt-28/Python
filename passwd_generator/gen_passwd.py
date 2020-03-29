#!/usr/bin/python3.7

import random
import re
import secrets
import string
import pyperclip
import time
import os

def func_clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def func_gen_password():
    len_passwd = random.randint(16, 32)
    alphabet = string.ascii_letters
    numeric = string.digits
    symbols =string.punctuation

    while True:
        password = ''.join(secrets.choice(alphabet + numeric + symbols) for i in range(len_passwd))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    return password


def func_countdown(delay):
    # Loops thru & prints time left to clear clipboard
    sleep_time_in_sec = delay
    while True:
        print ('password copied to clipboard!')
        print("Password will be cleared out in", sleep_time_in_sec)
        time.sleep(1)
        sleep_time_in_sec = (sleep_time_in_sec - 1)
        func_clear_console()
        if sleep_time_in_sec == 0:
            break  


def func_clip_clear_payload(generated_password):
    # Clip password
    pyperclip.copy(generated_password)

    func_countdown(15)

    # Clear clipboard
    pyperclip.copy("")
    print ('Password cleared from clipboard!')


# clear console
func_clear_console()

# generate password
gen_password = func_gen_password()

# clip n clear password
func_clip_clear_payload(gen_password)
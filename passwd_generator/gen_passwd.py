#!/usr/bin/python3.7

import random
import re
import secrets
import string
import pyperclip

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

# print (password)
pyperclip.copy(password)
result = pyperclip.paste()

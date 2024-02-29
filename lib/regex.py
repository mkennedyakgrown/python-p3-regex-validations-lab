import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"John Cena|Anya Taylor-Joy|D'Angelo"
name_regex = re.compile(name)

phone_number = r"5{10}|555\W555\W5555|\W555\W\s555\W5555"
phone_regex = re.compile(phone_number)

email_address = r"\b[A-z]+[A-z0-9._%+-]+@[A-z-0-9]+\.[A-z]{2,}\b"
email_regex = re.compile(email_address)

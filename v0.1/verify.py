import re

def phone_check(number):
    pattern1 = r"^[0-9]{10}$"
    pattern2 = r"^[+]?[0-9]{2}$[\s?][0-9]{10}"
    if re.match(pattern1, str(number)) or re.match(pattern2, str(number)): return True
    else: return False

def email_check(email):
    pattern1 = r"^([\w]+)@([a-zA-Z]+).(com)$"
    pattern2 = r"^([\w]+)@([a-zA-Z]+).(net)$"
    pattern3 = r"^([\w]+)@([a-zA-Z\.]+).(au)$"
    if re.match(pattern1, str(email)) or re.match(pattern2, str(email)) or re.match(pattern3, str(email)): return True
    else: return False

def name_check(name):
    pattern = r"^[a-zA-Z]+$"
    if re.match(pattern, str(name)): return True
    else: return False
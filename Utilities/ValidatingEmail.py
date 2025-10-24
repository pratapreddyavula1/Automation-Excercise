import re
import  datetime
from Utilities.readProperties import Readconfig

def validating_email(mail):
    match = re.fullmatch(r"[a-zA-Z0-9._]+@[a-zA-Z]{5}\.com$", mail)
    if match:
        return True
    else:
        return False
def cc_number(CC):
    match=re.fullmatch(r"^(?!.*(\d)\1{3})(\d{4}\s?){4}$",CC)
    if match:
        return True
    else:
        return False
def cvc(CVC):
    match=re.fullmatch(r"\d{3}",CVC)
    if match:
        return True
    else:
        return False
def year(m):
    year=datetime.date.today().year
    match = re.search(r"\d{4}", m)
    if match:
        if int(match.group())>year:
            return True

    else:
        print("Entered value is less than Current Year")
        return False

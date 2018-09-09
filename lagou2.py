import requests
import re
import hashlib

username='18381668790'
password='zz22731277'

def md5(s):
    m2 = hashlib.md5()
    m2.update(s)
    return m2.hexdigest()

def passwordMD5(p):
    y = "veenike"
    return md5(y + md5(p) + y)


ua1="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36Name"
ua2="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36"
ua=ua1

session = requests.session()
r1 = session.get(
    "https://passport.lagou.com/login/login.html",
    headers = {
        "User-Agent":ua
        # "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36"
    }
)
X_Anit_Forge_Code  = re.findall(r"X_Anti_Forge_Code = '(.*?)'", r1.text, re.S)[0]
X_Anit_Forge_Token = re.findall("X_Anti_Forge_Token = '(.*?)'", r1.text, re.S)[0]
r2 = session.post(
    "https://passport.lagou.com/login/login.json",
    headers = {
        "User-Agent":ua,
        "Referer":"https://passport.lagou.com/login/login.html",
        "X-Anit-Forge-Code":X_Anit_Forge_Code,
        "X-Anit-Forge-Token":X_Anit_Forge_Token,
        "X-Requested-With":"XMLHttpRequest"
    },
    data={
        "isValidate": True,
# 'username': '18611453110',
# 'password': '70621c64832c4d4d66a47be6150b4a8e',
        'username': username,
        'password': passwordMD5(password),
        'request_form_verifyCode': '',
        'submit': ''
    }
)
print r2.text
r3 = session.get(
    "https://passport.lagou.com/grantServiceTicket/grant.html",
    headers = {
        "User-Agent": ua,
        'Referer': 'https://passport.lagou.com/login/login.html',
    }
)


url ="https://www.lagou.com/center/preview.html"#"https://www.lagou.com/resume/myresume.html"
r3=session.get(url)
print r3.text


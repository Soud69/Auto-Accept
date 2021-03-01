try:
    import requests
    import time
    import uuid
    import json
    import os
    from os import system
    system("title " + "Soud Was Here - @_agf - Soud#0737 - Auto-Accept V1")
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()

print("""
    ░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
    ██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
    ╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
    ░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
    ██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
    ╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
                              """, Fore.GREEN + "Credit @_agf - Soud#0737")
print(Fore.GREEN + "Auto-Accept By Soud,", Fore.RED+"Free And Not For Sell\n")
username = str(input("Enter Your Username: "))
password = str(input("Enter Your Password: "))
slee = int(input("Enter Sleep sec (3s Normal): "))
uid = str(uuid.uuid4())
cok = ""
hh = ""
hd_login = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com'
}
checked = 0
acceptdone = 0
unaccepted = 0


def get_challenge_choices(last_json):
    choices = []

    if last_json.get("step_name", "") == "select_verify_method":
        choices.append("Challenge received")
        if "phone_number" in last_json["step_data"]:
            choices.append("0 - Phone")
        if "email" in last_json["step_data"]:
            choices.append("1 - Email")

    if last_json.get("step_name", "") == "delta_login_review":
        choices.append("Login attempt challenge received")
        choices.append("0 - It was me")
        choices.append("0 - It wasn't me")

    if not choices:
        choices.append(
            '"{}" challenge received'.format(last_json.get("step_name", "Unknown"))
        )
        choices.append("0 - Default")

    return choices


def challange(login_json):
    global cok, hh
    challenge_url = 'https://i.instagram.com/api/v1/' + login_json["challenge"]["api_path"][1:]
    try:
        b = requests.get(challenge_url, headers=hd_login, cookies=cok)
    except Exception as e:
        print("solve_challenge; {}".format(e))
        return False
    choiccc = get_challenge_choices(b.json())
    for choice in choiccc:
        print(choice)
    code = input("Insert choice : ")
    data_c = {
        'choice': code,
        '_uuid': uid,
        '_uid': uid,
        '_csrftoken': 'missing'
    }
    send_c = requests.post(challenge_url, data=data_c, headers=hd_login, cookies=cok)
    print("A code has been sent to {}, please check.".format(send_c.json()['step_data']['contact_point']))
    code = input("Insert code: ").strip()
    data_co = {
        'security_code': code,
        '_uuid': uid,
        '_uid': uid,
        '_csrftoken': 'missing'
    }
    send_o = requests.post(challenge_url, data=data_co, headers=hd_login, cookies=cok)
    send_coj = send_o.json()
    if 'logged_in_user' in send_coj:
        print(Fore.GREEN + f"Logged in >> @{username}")
        hh = send_o.cookies
        if 'is_private":false,' in send_o.text:
            print(Fore.RED + "Account Is Not Private, Changing now")
            private()
        ggtt()
        return True
    return False


def login_api():
    global hd_login, cok, hh
    login_url = "https://i.instagram.com/api/v1/accounts/login/"
    data_login = {'uuid': uid,
                  'password': password,
                  'username': username,
                  'device_id': uid,
                  'from_reg': 'false',
                  '_csrftoken': 'missing',
                  'login_attempt_count': '0'}
    loginc = requests.post(login_url, data=data_login, headers=hd_login)
    login1 = loginc.text
    if '"logged_in_user"' in login1:
        print(Fore.GREEN+f"Logged in >> @{username}")
        hh = loginc.cookies
        if 'is_private":false,' in login1:
            print(Fore.RED+"Account Is Not Private, Changing now")
            private()

        ggtt()
    elif "The username you entered doesn't appear to belong to an account" in login1:
        print(Fore.RED+f"Wrong Username >> @{username}")
        time.sleep(3)
        exit()
    elif "The password you entered is incorrect" in login1:
        print(Fore.RED+f"Wrong Password >> @{username}")
        time.sleep(3)
        exit()
    elif '"inactive user"' in login1:
        print(Fore.RED+f"Banned Account >> @{username}")
        time.sleep(3)
        exit()
    elif "checkpoint_challenge_required" in login1:
        cok = loginc.cookies
        return challange(loginc.json())
    elif 'two_factor_required":true,':
        print(Fore.RED+f"Found 2Factor, Pls Turn It Off And Try Again >> @{username}")
        time.sleep(3)
        exit()


def private():
    global hd_login, hh
    url = "https://i.instagram.com/api/v1/accounts/set_private/"
    data = {
        "is_private": "true"
    }
    see = requests.post(url, data=data, headers=hd_login, cookies=hh)
    if 'is_private":true,' in see.text:
        print(Fore.GREEN+"Done Changing To Private")
        grabid()
    else:
        print(Fore.RED+"Something Went Wrong")
        print(see.text)


def grabid():
    global hd_login, hh, acceptdone, checked, unaccepted
    url = "https://i.instagram.com/api/v1/friendships/pending/?rank_mutual=0"
    ree = requests.get(url, headers=hd_login, cookies=hh)
    if 'users":[],' in ree.text:
        time.sleep(4)
        ggtt()
    else:
        checked += 1
        jj = json.loads(ree.text)
        userr = jj["users"][0]["username"]
        idd = jj["users"][0]["pk"]
        acceptuser(userr, idd)


def acceptuser(userr, idd):
    global hd_login, hh, checked, unaccepted, acceptdone
    url = f"https://i.instagram.com/api/v1/friendships/approve/{idd}/"
    acce = requests.post(url, headers=hd_login, cookies=hh)
    if 'status":"ok' in acce.text:
        acceptdone += 1
        print(Fore.GREEN+f"Accepted: @{userr} - Checked: {checked} - Done: {acceptdone} - Error: {unaccepted}")
    else:
        unaccepted += 1
        print(Fore.RED + f"Error: @{userr} - Checked: {checked} - Done: {acceptdone} - Error: {unaccepted}")


def ggtt():
    while 1:
        grabid()
        time.sleep(slee)


login_api()

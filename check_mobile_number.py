from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

print("╔═╗┬ ┬┌─┐┌─┐┬┌─  ╔╦╗┌─┐┌┐ ┬┬  ┌─┐  ╔╗╔┬ ┬┌┬┐┌┐ ┌─┐┬─┐")
print("║  ├─┤├┤ │  ├┴┐  ║║║│ │├┴┐││  ├┤   ║║║│ ││││├┴┐├┤ ├┬┘")
print("╚═╝┴ ┴└─┘└─┘┴ ┴  ╩ ╩└─┘└─┘┴┴─┘└─┘  ╝╚╝└─┘┴ ┴└─┘└─┘┴└─")
print("             Created by : Single Core\n")

# Enter phone number like that i writed here ----> +Contry code then number ----> +1000000000
number = input("Enter the phone number: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(phone)
print(time)
print(car)
print(reg)

def is_mobile_number_active(number):
    url = f"https://api4.truecaller.com/v1/search?phone={number}&countryCode=BD&type=4&locAddr=&placement=SEARCHRESULTS%2CHISTORY%2CDETAILS&encoding=json"
    headers = {
        "Authorization": "Bearer <your_truecaller_api_key>",
        "User-Agent": "Truecaller/11.59.5 (Android;10)",
        "Accept-Encoding": "gzip"
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if response.status_code == 200:
            if data["status"] == 200:
                if data["data"][0]["internationalFormat"] == num:
                    return True
        return False
    except:
        return False

# Example usage
# Enter number like that i writed here ----> 09000000000
num = input("Enter the phone num again to see active: ")
active = is_mobile_number_active(num)
print(f"The mobile number {num} is {'active' if active else 'not active'}.")

from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import re

print("╔═╗┬ ┬┌─┐┌─┐┬┌─  ╔╦╗┌─┐┌┐ ┬┬  ┌─┐  ╔╗╔┬ ┬┌┬┐┌┐ ┌─┐┬─┐")
print("║  ├─┤├┤ │  ├┴┐  ║║║│ │├┴┐││  ├┤   ║║║│ ││││├┴┐├┤ ├┬┘")
print("╚═╝┴ ┴└─┘└─┘┴ ┴  ╩ ╩└─┘└─┘┴┴─┘└─┘  ╝╚╝└─┘┴ ┴└─┘└─┘┴└─")
print("             Created by : Single Core\n")

def extract_country_code(phone_number):
    # Define the regex pattern to match the country code
    pattern = r'^\d{2}'

    # Use the re.search() function to find the country code in the phone number
    match = re.search(pattern, phone_number)

    if match:
        # Extract the matched country code
        country_code = match.group()
        return country_code
    else:
        return None

# Dictionary that maps country codes to country names or abbreviations
country_codes = {
    '01': {'name': 'USA', 'code': '+1'},
    '02': {'name': 'Canada', 'code': '+1'},
    '03': {'name': 'UK', 'code': '+44'},
    '04': {'name': 'Australia', 'code': '+61'},
    '05': {'name': 'New Zealand', 'code': '+64'},
    '06': {'name': 'India', 'code': '+91'},
    '07': {'name': 'Singapore', 'code': '+65'},
    '08': {'name': 'Malaysia', 'code': '+60'},
    '09': {'name': 'Indonesia', 'code': '+62'},
    '10': {'name': 'Thailand', 'code': '+66'},
    '98': {'name': 'Iran', 'code': '+98'},
    # Add more country codes and abbreviations as needed
}

# Example usage
print("Help: Do not enter 0 for 98 and 10, and if my tool says country code not found, you can visit to this site : https://locatemate.co")
print("""Country codes:
    01:name: USA, code: +1
    02:name: Canada, code: +1
    03: name: UK, code: +44
    04: name: Australia, code: +61
    05: name: New Zealand, code: +64
    06: name: India, code: +91
    07: name: Singapore, code: +65
    08: name: Malaysia, code: +60
    09: name: Indonesia, code: +62
    10: name: Thailand, code: +66
    98: name: Iran, code: +98""")
phone_numbers = input("Enter phone number to find country code or click enter to skip:")

for phone_number in phone_numbers:
    country_code = extract_country_code(phone_number)

    if country_code:
        # Look up the country name or abbreviation in the dictionary
        country_info = country_codes.get(country_code)
        if country_info:
            print(f"The number is {phone_number} and country code is {country_info['code']} ({country_info['name']})")
    else:
        print("Country code not found.")
# Enter phone number like that i writed here ----> +Contry code then number ----> +1000000000
print("Enter the phone number with country code to see where is the user of the sim.")
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
print(f"The mobile number {num} is {'active' if active else 'not active'}.\n")

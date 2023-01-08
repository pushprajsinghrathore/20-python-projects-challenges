# frist we install pip install phone number
import phonenumbers
from phonenumbers import timezone ,geocoder,carrier #  from phone number  me timezone,geocoder,carrier iimport kiya
number=input("Enter your number")
phone=phonenumbers.parse(number) # parse give a phone number detailes
time=timezone.time_zones_for_number(phone)
carr=carrier.name_for_number(phone,"en")  # carries moudle jo sim company name show krte he
region=geocoder.description_for_number(phone,'en')  # geocoder  use for counrty name
print(phone)
print(time)
print(carr)
print(region)
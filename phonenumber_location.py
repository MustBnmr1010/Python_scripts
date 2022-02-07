import phonenumbers
#dnt forget the country code 
number = input("Your number or other number : ")

key = "gp to opencagedata and make an account and get the api key."

from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
Location = geocoder.description_for_number(ch_number, "en")
print(Location)

from phonenumbers import carrier

service_number = phonenumbers.parse(number, "RO")

print(carrier.name_for_number(service_number, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)
query = str(Location)

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lang = results[0]['geometry']['lng']

print(lat, lang)
#preview the phone location
import folium
name = number+".html"
myMap = folium.Map(location=[lat, lang], zoom_start=9)
folium.Marker([lat, lang],popup=Location).add_to((myMap))
myMap.save(name)
lat_lng = lat+lang
v = ","
link = f'https://www.google.com/maps/@{lat+v+lang}z?hl=fr'
print("Check ur directory and enter this file : "+name)
print(f"NOTE! If the {name} didnt load perfectly go to this link : ",link)

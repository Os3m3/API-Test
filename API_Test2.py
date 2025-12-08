import requests as req
import pycountry as pyco

name = input("Enter the Person's Name: ")

response = req.get(f"https://api.nationalize.io/?name={name}")

result_json = response.json()

country_list = result_json["country"]

print(result_json["name"])

for countries in country_list:
    country_code = countries['country_id']
    full_country = pyco.countries.get(alpha_2=country_code)
    print(f"countries: {country_code} - {full_country.name}")
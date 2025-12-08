import requests

name = input("Enter the Person's Name: ")

response = requests.get(f"https://api.nationalize.io/?name={name}")

result_json = response.json()

county_list = result_json["country"]

print(result_json["name"])

for contries in county_list:
    print(contries["country_id"])


import requests

url = 'https://dummyjson.com/users'

params = {
    'limit': 350,
    'skip': 0
}
response = requests.get(url, params=params)
response_json = response.json()

users = response_json['users']

age_smaller_than_30 = 0
girs_with_grin_esey = 0
people_wich_live_in_San_Francisco = 0

for user in users:
    if user.get("age") < 30:
        age_smaller_than_30 += 1


for user in users:
    if user.get("gender") == 'female':
        if user.get("eyeColor") == 'Green':
            girs_with_grin_esey += 1


for user in users:
    if user.get("address", {}).get("city", "") == 'San Francisco':
        people_wich_live_in_San_Francisco += 1





print("people with age smaller than 30 -",age_smaller_than_30)
print("girs_with_grin_esey -",girs_with_grin_esey)
print("people_wich_live_in_San_Francisco -",people_wich_live_in_San_Francisco)

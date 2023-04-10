import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
resp = requests.get(url)
result = resp.json()
mind_of_heroes = {}
for i in result:
    key = i.get('name')
    if key in 'Captain America Hulk Thanos':
        val = i.get('powerstats').get('intelligence')
        mind_of_heroes.setdefault(key, val)
smartest = dict([max(mind_of_heroes.items(), key=lambda k_v: k_v[1])])
print(f'Самый умный из Captain America, Hulk, Thanos: {"".join(smartest.keys())}')

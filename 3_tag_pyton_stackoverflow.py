import requests
from pprint import pprint

url = 'https://api.stackexchange.com/2.3/questions?fromdate=1680912000&todate=1681084799&order=desc&sort=activity&tagged=python&site=stackoverflow'
resp = requests.get(url)
result = resp.json()
# pprint(result)
q_about_python = []
step_1 = result.get('items')
for i in step_1:
    q_about_python.append(i.get('title'))
print('Запросы с тэгом "python" за последние два дня:\n')
print("\n".join(q_about_python))
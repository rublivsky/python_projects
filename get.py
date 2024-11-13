import requests

print("start")

url = 'https://corruptinfo.nazk.gov.ua/ep/1.0/corrupt/getAllData123'
headers = {'Accept': 'text/plain'}

response = requests.get(url, headers=headers)

print("get requests sended")

print(response.status_code)
response_text = response.text

with open ("test_dp.txt", "w") as file:
    file.write(response_text)
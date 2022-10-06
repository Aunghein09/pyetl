import requests
from bs4 import BeautifulSoup

url = "https://testselect.uuboyscy.repl.co/"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "User-Agent": user_agent
}

data = {
    '1A': 'Apple',
    '2A': 'Dog',
    'cars': 'volvo',
    'subject1': 'Car Loan',
    'subject2': 'ogk',
    'subject3': 'xf'}

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "html.parser")
input_tag = soup.select('input[type="hidden"]')
for tag in input_tag:
    data[tag['name']] = tag['value']
print(data)

print(
    requests.post(
        "https://www.w3schools.com/action_page.php",
        headers = headers,
        data=data ).text
)

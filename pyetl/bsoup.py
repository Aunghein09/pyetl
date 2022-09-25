import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/photo/index.html"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "User-Agent": user_agent
}

# <class 'requests.models.Response'>
res = requests.get(url, headers=headers)

# assign a soup obj <class 'bs4.BeautifulSoup'> form Response.text
# html.parser arg is used to point the parser using,if not there will be a warning
soup = BeautifulSoup(res.text, "html.parser")

print(soup)
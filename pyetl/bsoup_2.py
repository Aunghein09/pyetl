import requests
from bs4 import BeautifulSoup


url = "https://www.ptt.cc/bbs/movie/index.html"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "User-Agent": user_agent
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# title_tag_list = soup.findAll('div', class_ ="title")
# can omit .findAll --> same as findAll
title_tag_list = soup('div', class_ ="title")

for title_tag_obj in title_tag_list:
    if title_tag_obj.select_one('a') == None:
        continue
    title_name = title_tag_obj.select_one('a').text
    article_url = "https://www.ptt.cc" + title_tag_obj.select_one('a')['href']

    print(title_name)
    print(article_url)
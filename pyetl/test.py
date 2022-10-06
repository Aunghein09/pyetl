import requests
from bs4 import BeautifulSoup

article_url = "https://www.ptt.cc/bbs/movie/M.1664022409.A.D11.html"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "User-Agent": user_agent
}

article_response = requests.get(article_url, headers=headers)

article_soup = BeautifulSoup(article_response.text, "html.parser")

article_tag_obj = article_soup.select_one('div[id="main-content"]')
article_content = article_tag_obj.text.split('※ 發信站:')[0]
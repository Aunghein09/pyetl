import string

import requests
from bs4 import BeautifulSoup
import os
import re


url = "https://www.ptt.cc/bbs/movie/index.html"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "User-Agent": user_agent
}

# create a new dir
if not os.path.exists("pttmovie"):
    os.mkdir("pttmovie")


for _ in range(5):
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
        # scraping the web content
        article_response = requests.get(article_url, headers=headers)

        article_soup = BeautifulSoup(article_response.text, "html.parser")
        # locate the tag
        article_tag_obj = article_soup.select_one('div[id="main-content"]')
        # parse and get_content
        article_content = article_tag_obj.text.split('※ 發信站:')[0]
        # err_char = ['/','?']
        # for c in err_char:
        #     if c in title_name:
        #         title_name.replace(c,'')
        # start saving into txt file
        #FileNotFoundError: [Errno 2] No such file or directory: 'pttmovie/[公告] 電影板板規 2021/9/4.txt'
        # file name contains '/' make computer this it's a directory

        try:
            with open("pttmovie/{}.txt".format(title_name), 'w', encoding="utf-8") as fhand:
                fhand.write(article_content)
        except FileNotFoundError:
            with open("pttmovie/{}.txt".format(title_name.translate(str.maketrans('','',string.punctuation))), 'w', encoding="utf-8") as fhand:
                fhand.write(article_content)
        except OSError:
            pass

        print(title_name)
        print(article_url)
        print('=' * 40)

    # updating the url to 上一頁
    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]['href']
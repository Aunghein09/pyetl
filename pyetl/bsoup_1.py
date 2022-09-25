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
# html.parser arg is used to point the parser using ->hmtl 字串 轉為可定位的形態
soup = BeautifulSoup(res.text, "html.parser")


# return <class 'bs4.element.ResultSet'> which is a list of <class 'bs4.element.Tag'> and its contents that fulfill the find args
# logo_tag_list = soup.findAll('a', {'id': 'logo'})
# logo_tag_list = soup.findAll('a', id = 'logo')

logo_tag_list = soup.findAll('a', class_ = 'right small', href= '/about.html') # class keyword --> add _ to the name
print(logo_tag_list)
# .text gives the content of that particular tag
print(logo_tag_list[0].text)

# tag obj attributes can be thought of as a dict
print(logo_tag_list[0]['href'])
# print(logo_tag_list[0]['id'])

print("==================================================")
# select method
# title_tag_list = soup.select('div[class="title"]')
title_tag_list = soup.findAll('div',class_ = 'title')

'''
<div class="title">
<a href="/bbs/photo/M.1660991759.A.8F6.html">[作品] 生活在台南</a>
</div>
'''
print(title_tag_list[0])
# go deeper into the subtag using select once more --> select returns list; select_one returns a tag obj
# title_detail_tag = title_tag_list[0].select_one('a')
title_detail_tag = title_tag_list[0].find('a')

print(title_detail_tag)


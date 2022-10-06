import requests
url = "https://www.ptt.cc/bbs/Gossiping/index.html"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "User-Agent": user_agent
}

# assign cookies
# cookies = {
#     "over18" : "1"
# }
# response = requests.get(url, headers = headers, cookies=cookies)
ss = requests.session()
ss.cookies["over18"] = '1'
# after this, cookies is attached throughout the upcoming session
response = ss.get(url, headers=headers)


print(response.text)
from urllib import request

# assign a url address to a variable
# url = "https://5278-13-231-145-110.ngrok.io/hello_get?name=Allen"
#
# # return a http.client.HTTPResponse object
# # res = request.urlopen(url=url)
#
# # read the content of the object --> byte obj ; decode --> string
# print(res.read().decode("utf-8"))

# # this inhibits the web scrapping without user agent --> 403 forbidden
url = "https://www.ptt.cc/bbs/photo/index.html"
# res = request.urlopen(url = url)
# print(res.read().decode("utf-8"))


# adding user_agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
# create header (dict) with required information
headers = {
    "User-Agent": user_agent
}
# creat a request obj <class 'urllib.request.Request'>
req = request.Request(url=url, headers=headers)
print(type(req))
# this time open the Request obj
# ~ file handle
res = request.urlopen(req)
# beware that read as usual has cursor
print(res.read().decode("utf-8"))
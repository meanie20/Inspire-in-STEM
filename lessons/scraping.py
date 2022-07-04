import requests
from bs4 import BeautifulSoup as bs
user_name="meanie20" #input username
url='https://github.com/'+user_name     #input("Enter url site")
result = requests.get(url)

soup= bs(result.content,"html.parser")
profile_pic = soup.find("img",{"alt":"Avatar"})["src"]
print(profile_pic)
name= soup.find

#get the username

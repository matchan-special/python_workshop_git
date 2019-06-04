import urllib.request
import requests
from bs4 import BeautifulSoup
import time

class Scraper:
  def __init__(self, site):
    self.site = site

  def scrape_pornactress(self):
    time.sleep(2)
    site_url = self.site
    r = urllib.request.urlopen(site_url)
    html = r.read()
    parser = "html.parser"
    sp = BeautifulSoup(html, parser)
    
    div = sp.find("div", attrs={"class", "d-sect act-box"})
    li  = div.find_all("li")
    actress_list = []
    for i in li:
      name_kana = i.find("span").string
      name = i.find("img").get("alt")
      pic  = i.find("img").get("src")
      actress_list.append((name, name_kana))
      pic_data = requests.get(pic).content
      with open(str(name)+str(".jpeg"), "wb") as f:
        f.write(pic_data)
    
    with open("actress_name.txt", "w") as f:
      for j in actress_list:
        f.write(j[0] + "  " + "(" + j[1] + ")" + "\n")

# 実行

fanza = "https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=a/"

test = Scraper(fanza)
test.scrape_pornactress()

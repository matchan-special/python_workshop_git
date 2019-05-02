import urllib.request
from bs4 import BeautifulSoup

class Scraper:
  def __init__(self, site, sp, urls):
    self.site = site
    self.sp = sp
    self.urls = urls

  def scrape(self):
    r = urllib.request.urlopen(self.site)
    html = r.read()
    parser = "html.parser"
    sp = BeautifulSoup(html, parser)
    count = 0

    with open(self.sp, mode='w') as f_sp:
      f_sp.write(str(sp))

    with open(self.urls, mode='w') as f_urls:
      for tag in sp.find_all("a", attrs={"class", "DY5T1d"}):
        gaiyou = tag.string
        url    = tag.get("href")
        if url is None:
          continue
        count += 1
        f_urls.write(str(count) + " " + gaiyou + "\n" + "https://news.google.com/" + url + "\n")


#news = "https://news.google.com/?hl=ja&gl=JP&ceid=JP%3Aja"
news = "https://news.google.co.jp/"
file1 = "sp_google.txt"
file2 = "urls_google.txt"

Scraper(news, file1, file2).scrape()

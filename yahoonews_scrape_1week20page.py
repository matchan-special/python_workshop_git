import urllib.request
from bs4 import BeautifulSoup
import datetime
import time

class Scraper:
  def __init__(self, site, sp, urls):
    self.site = site
    self.sp = sp
    self.urls = urls
  
  def scrape_1week(self):
    
    # create date list
    dates = [] 
    for i in range(7):
      today = datetime.date.today()
      tar   = today - datetime.timedelta(days = i)
      tar_str = str(tar).replace("-", "")
      dates.append(tar_str)
    
    # open file
    with open(self.urls, mode='w') as f_urls:
      
      # 1week
      for j in dates:
        f_urls.write(j + "\n")
        count = 0
        
        # 20pages
        for k in range(1,20):
          time.sleep(2) 
          # High speed scrayping would be DoS attack. sleep(2) take 2 seconds.
          site_url = self.site + j + "&p=" + str(k)
          r = urllib.request.urlopen(site_url)
          html = r.read()
          parser = "html.parser"
          sp = BeautifulSoup(html, parser)
          
          li = sp.find_all("li", attrs={"class", "ListBoxwrap"})
          for l in li:
            a      = l.find("a")
            if a is None:
              continue
            url    = a.get("href")
            dt     = l.find("dt")
            gaiyou = dt.string
            
            count += 1
            f_urls.write(str(count) + " " + gaiyou + "\n" + url + "\n")


news = "https://news.yahoo.co.jp/list/?d="
file1 = "sp.txt"
file2 = "urls.txt"

Scraper(news, file1, file2).scrape_1week()

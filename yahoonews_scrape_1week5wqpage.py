import urllib.request
from bs4 import BeautifulSoup
import datetime
import time
from janome.tokenizer import Tokenizer
import collections

class Scraper:
  def __init__(self, site):
    self.site = site
    self.news_list = []
    self.noun_list = []
  
  def scrape_1week(self):   
    # create date list
    dates = [] 
    for i in range(7):
      today = datetime.date.today()
      tar   = today - datetime.timedelta(days = i)
      tar_str = str(tar).replace("-", "")
      dates.append(tar_str)
      
    # 1week
    for j in dates:
      # 5pages 
      for k in range(1,5):
        time.sleep(2) 
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
          self.news_list.append((gaiyou,url))
  
  def token_analysis(self):
    t = Tokenizer()
    for m in self.news_list:
      for token in t.tokenize(m[0]):
        if token.part_of_speech.startswith('名詞,一般') is True:
          self.noun_list.append(token.surface)
    
    self.noun_count = collections.Counter(self.noun_list)
    self.noun_top10 = self.noun_count.most_common(10)

  def extract_top10news(self):
    for n in self.noun_top10:
      target_noun = n[0]
      print("名詞:", target_noun)
      for o in self.news_list:
        if target_noun in o[0]:
          print(o)
      print("\n")


news = "https://news.yahoo.co.jp/list/?d="

test = Scraper(news)
test.scrape_1week()
test.token_analysis()
test.extract_top10news()

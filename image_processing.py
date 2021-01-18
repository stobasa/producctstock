import sys
import numpy as np
import pandas as pd
import pymysql
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

def get_image(product):
  driver.get("https://www.google.com/webhp?tbm=shop&sxsrf=")
  driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(product)
  driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(Keys.ENTER)
  soup=BeautifulSoup(driver.page_source, 'lxml')
  div=soup.find('div',{"class":"JRlvE XNeeld"})
  image_link = div.find('img').attrs['src']
  return image_link


data = pd.read_csv("datafeed.csv")
data["RRPEx"] = data["RRPEx"].str.replace(',', '')
data["RRPEx"] = data["RRPEx"].astype(float)
df = data[data["RRPEx"]>= 2]
df["images"] = get_image(df["StockCode"])

number_images = len(df["images"])
sku_change = len(data["StockCode"]) - len(df["StockCode"])





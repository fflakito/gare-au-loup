# from https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import sys
import urllib3
import argparse
import urllib.request

searchterm = sys.argv[1] # user-input of type string
scroll_nums = int(sys.argv[2]) # user-input of type int (a few dozens or hundreds)

url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"

# CHROMEDRIVER to be downloaded by user => https://chromedriver.chromium.org/
print("Opening browser...")
browser = webdriver.Chrome("./chromedriver")
print("Browser is querying search url...")
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

counter = 0
succounter = 0

print("Scrolling to generate more images on the page...")
for _ in range(scroll_nums):
    browser.execute_script("window.scrollBy(0,10000)")

print("Scraping ...")
for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd tx8vtf")]'):
    counter = counter + 1
    # print("URL:", x.get_attribute('src'))

    img = x.get_attribute('src')
    new_filename = "image"+str(counter)+".jpg"

    try:
        path = './dl/'
        path += new_filename
        urllib.request.urlretrieve(img, path)
        succounter += 1
    except Exception as e:
        print(e)

print("Total Count:", counter)
print("Successful Count:", succounter)

print(succounter, "pictures succesfully downloaded")
browser.close()

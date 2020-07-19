import os
from selenium import webdriver

def get_driver():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    drivers_dir = os.path.join(root_dir,'chromedriver_mac64')
    return drivers_dir

def open_website(chrome, url):
    chrome.get(url)
    chrome.implicitly_wait(10)

def get_books_comment(chrome):
    comments=chrome.find_elements_by_css_selector("[class='section']>div.reviews-bd>div.review>div.review-bd>div.review-content")
    j = len(comments)
    i = 0
    while i < j:
        comment = comments[i].text
        print(comment)
        i+=1

get_driver_path = get_driver()
chrome = webdriver.Chrome(get_driver_path)
url = "https://book.douban.com/"
open_website(chrome,url)
get_books_comment(chrome)
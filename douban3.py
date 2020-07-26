#豆瓣读书首页第一屏图书封面图下载，图片命名为书名，存放到指定路径
import os
from selenium import webdriver
import urllib.request

def get_driver():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    drivers_dir = os.path.join(root_dir,'chromedriver_mac64')
    return drivers_dir

def open_wbsite(chrome,url):
    chrome.get(url)
    chrome.implicitly_wait(10)

def get_books(chrome):
    picture_urls= chrome.find_elements_by_css_selector("[class='list-col list-col5 list-express slide-item']>li>div.cover>a>img") #查找出所有节点
    j = len(picture_urls)
    i = 0
    while i < j:
        element=picture_urls[i] #节点集合中的第i项赋值给element
        picture_url=element.get_attribute('src') #element中的src属性赋值给picture_url
        title=element.get_attribute('alt') #element中的alt属性赋值给title
        urllib.request.urlretrieve(picture_url,'/Users/hui/Downloads/pictures/'+title+'.jpg')
        #调用urllib.request.urlretrieve方法，打开图片链接，并保存到指定文件夹，以title命名
        i+=1

get_driver_path = get_driver()
chrome = webdriver.Chrome(get_driver_path)
url = "https://book.douban.com/"
open_wbsite(chrome, url)
get_books(chrome)



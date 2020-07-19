import os
import time
from selenium import webdriver
#定义一个获取脚本路径的方法
def get_driver():
    root_dir = os.path.dirname(os.path.abspath(__file__)) #返回当前脚本的绝对路径目录
    drivers_dir = os.path.join(root_dir, 'chromedriver_mac64') #在返回的路径后面添加chromedriver_mac64
    return drivers_dir
#定义一个打开网页的方法
def open_website(chrome, url):
    chrome.get(url) #打开url
    chrome.implicitly_wait(10) #等待10
#定义一个点击翻页按钮的方法
def click_button(chrome):
    if chrome.find_element_by_css_selector(
            "[class='section books-express ']>div.hd>div.slide-controls>div.slide-btns>a.next"): #先判断是否找到翻页按钮
        chrome.find_element_by_css_selector(
            "[class='section books-express ']>div.hd>div.slide-controls>div.slide-btns>a.next").click() #点击翻页按钮
#定义一个获取书名的方法，给该方法传递当前点击次数r，获取r*10+i个书名，循环中每次获取10个，因为每页都是10个
def get_books_list(chrome, r):
    i = 0
    while i <10:
        book_name =  chrome.find_elements_by_css_selector(
            "[class='list-col list-col5 list-express slide-item']>li>div.info>div.title>a")[r*10+i].text
        print(book_name)
        i+=1

get_driver_path = get_driver() #获取脚本路径并执行
chrome = webdriver.Chrome(get_driver_path) #调用webdriver.Chrome()方法并赋值给chrome
url = "https://book.douban.com/" #给url赋值
open_website(chrome, url) #打开网页
get_books_list(chrome,0) #第一次获取书名
#进入点击和获取的循环
j = 1
while j < 4:
    time.sleep(0.5)
    click_button(chrome) #先点击
    time.sleep(0.5)
    get_books_list(chrome,j) #获取书名，将j传递给r，j初始值为1，即第二次获取书名是第10-19个，第三次第四次以此类推，直到j<4停止循环
    j+=1

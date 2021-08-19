import sys
from urllib.request import urlopen
from urllib.request import FancyURLopener
import pandas as pd
import numpy as np
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('/Applications/BrynMawr/chromedriver')


def get_product_info(product_url):
    global browser
    browser.get(product_url)

    # close pop-up window
    try:
        login_window = browser.find_element_by_class_name('css-fslzaf').click()
    except (NoSuchElementException, ElementNotVisibleException) as exceptions:
        pass

    # scroll the page with Keys.PAGE_DOWN
    elements = browser.find_element_by_tag_name('body')
    for i in range(30):
        elements.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)


# def get_page_number(brand_url):
#     global browser
#     browser.get(brand_url)
#     time.sleep(1)
#     page_number = 1
#     pages = browser.find_element_by_class_name('')


# def get_product_list(product_type, base_url):
#     global browser
#     products_page_count = get_page_count(base_url)
#     product_list = []
#     for i in range(1, products_page_count + 1):
#         page_url = base_url + "?currentPage=" + str(i)
#         browser.get(page_url)
#         time.sleep(1)
#         elem = browser.find_element_by_tag_name("body")

#         no_of_pagedowns = 20

#         while no_of_pagedowns:
#             elem.send_keys(Keys.PAGE_DOWN)
#             time.sleep(0.2)
#             no_of_pagedowns -= 1

#         post_elems = browser.find_elements_by_class_name("css-ix8km1")

#         for post in post_elems:
#             product_name = post.get_attribute('aria-label')
#             product_link = post.get_attribute('href')
#             product_list.append([product_name, product_link])
#     df = pd.DataFrame(product_list, columns=['product_name', 'product_link'])
#     df.to_csv('tmp/'+product_type+'_product_list.csv', index=True)

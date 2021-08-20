import sys
from urllib.request import urlopen
from urllib.request import FancyURLopener
import pandas as pd
import numpy as np
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Applications/BrynMawr/chromedriver')


# def get_product_info(driver, product_url):
#     driver.get(product_url)

#     # close pop-up window
#     try:
#         login_window = driver.find_element_by_class_name('css-fslzaf').click()
#     except (NoSuchElementException, ElementNotVisibleException) as exceptions:
#         pass

#     # scroll the page with Keys.PAGE_DOWN
#     elements = driver.find_elements_by_tag_name('body')
#     for i in range(30):
#         elements.send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.3)


# def get_product_review(driver, product_url):
product_url = 'https://www.sephora.com/product/lotus-youth-preserve-dream-face-cream-P440312?skuId=2175560'
driver.get(product_url)
# reviews = driver.find_elements_by_class_name('css-13o7eu2 eanm77i0')
# print(reviews)
# for review in reviews:
#     review.click()
#     ratings = driver.find_element_by_class_name('css-1s11tbv eanm77i0')
#     print(ratings)

total_reviews_elem = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "css-13o7eu2 eanm77i0")))
total_reviews_text = total_reviews_elem.text
print(total_reviews_text)

next_comments = driver.find_element_by_class_name('css-13o7eu2 eanm77i0')
max_load_count = 84
# load all reviews
while next_comments and max_load_count:
    next_comments.click()
    next_comments = browser.find_element_by_class_name('css-1phfyoj')
    next_comments = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "css-1s11tbv.eanm77i0")))
    max_load_count -= 1

# css-1s11tbv eanm77i0

# correct syntax:
# driver.find_elements_by_class_name('css-13o7eu2.eanm77i0')
# css-1s11tbv eanm77i0

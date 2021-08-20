# credit for this code: https://github.com/LenaNevel/CAPSTONE/blob/master/00_getting_slugs.ipynb

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

from time import sleep
from random import randint
import pickle

option = webdriver.ChromeOptions()
driver = webdriver.Chrome('/Applications/BrynMawr/chromedriver')

# this list represents different skin care categories to collect
categories = ['moisturizing-cream-oils-mists',
              'cleanser',
              'facial-treatments',
              'eye-treatment-dark-circle-treatment',
              'facial-treatment-masks',
              'sunscreen-sun-protection',
              'lip-treatments']


# creates a function that gets the browser to scroll all down
def scroll_down(driver, number_of_scrolls):
    body = driver.find_element_by_tag_name('body')

    while number_of_scrolls >= 0:
        body.send_keys(Keys.PAGE_DOWN)
        number_of_scrolls -= 1

    return driver


# create an empty dataframe to store all product links by category
dataframe = pd.DataFrame(columns=['category', 'URL'])


def get_product_links(driver, category):
    global dataframe
    page_number = 1

    while True:
        url = 'https://www.sephora.com/shop/' + category + \
            '?pageSize=300&currentPage=' + str(page_number)
        driver.get(url)
        time.sleep(20)

        try:
            # check to see if the page is empty
            if driver.find_element_by_class_name('css-3a7b4s').is_displayed():
                break
        except:
            # check to see if there is a pop up windew
            try:
                # exit the pop up window
                xpath = '//*[@id="modalDialog"]/button'
                btn = driver.find_element_by_xpath(xpath)
                btn.click()
                time.sleep(20)
            except:
                pass

            # as scrolling check if there is any more room to scroll
            old_len = 0
            while True:
                browser = scroll_down(driver, 20)  # scroll down the page
                time.sleep(10)  # give it time to load
                slug = driver.find_elements_by_class_name(
                    'css-ix8km1')  # look for the urls of products
                new_len = len(slug)
                if old_len == new_len:  # if the old length and new length are equal, the bottom of page was reached
                    break
                else:
                    old_len = new_len

             # from the list of URLs in slug pull all the href and make a dictionary with it and the category name
            slugURL = []
            for a in slug:
                subURL = {}
                subURL['category'] = category
                subURL['URL'] = a.get_attribute('href')
                slugURL.append(subURL)

            # append our data frame with categories and URLs
            df = pd.DataFrame(slugURL)
            # print(df.head())
            # adding to go to next page
            page_number += 1

            # concatenating to get all in same df
            final_df = pd.concat([final_df, df], axis=0, ignore_index=True)


driver.close()

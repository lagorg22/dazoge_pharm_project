from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import random
from item_cls import Item

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=edge_options)

driver.get('https://psp.ge/catalogsearch/result?q=ana')
# print(len())
max_page = max([int(num.text) for num in WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'li[class="number"]')))])
print(max_page)

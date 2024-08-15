# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# import time
# from item_cls import Item
# import json
#
#
# class Pharmadepot:
#     def __init__(self, driver: webdriver, website, search_box_xpath, photo_xpath, name_xpath, price_xpath, country_xpath, link_xpath):
#         self.__driver = driver
#         self.__website = website
#         self.__search_box_xpath = search_box_xpath
#         self.__photo_xpath = photo_xpath
#         self.__name_xpath = name_xpath
#         self.__price_xpath = price_xpath
#         self.__country_xpath = country_xpath
#         self.__link_xpath = link_xpath
#         self.__items = []
#
#     def __search_for_items(self, word: str):
#         self.__driver.get(self.__website)
#         time.sleep(2)
#
#         search_box = self.__driver.find_element(by=By.XPATH, value=self.__search_box_xpath)
#         search_box.send_keys(word)
#         search_box.send_keys(Keys.RETURN)
#         time.sleep(5)
#
#         wait = WebDriverWait(self.__driver, 10)
#
#         names = [name.text for name in wait.until(ec.presence_of_all_elements_located((By.XPATH, self.__name_xpath)))]
#         countries = [country.text for country in
#                      wait.until(ec.presence_of_all_elements_located((By.XPATH, self.__country_xpath)))]
#         prices = [float(price.text.replace('\n', '').replace('₾', '')) for price in
#                   wait.until(ec.presence_of_all_elements_located((By.XPATH, self.__price_xpath)))]
#         photo_sources = [photo.get_attribute('src') for photo in
#                          wait.until(ec.presence_of_all_elements_located((By.XPATH, self.__photo_xpath)))]
#         links = [elem.get_attribute('href') for elem in
#                  wait.until(ec.presence_of_all_elements_located((By.XPATH, self.__link_xpath)))]
#
#         for i in range(len(prices)):
#             self.__items.append(Item(pharmacy='Pharmadepot', name=names[i], price=prices[i], photo_source=photo_sources[i], link=links[i], country=countries[i]))
#
#         # self.__driver.close()
#
#     def show_items(self, word):
#         if not len(self.__items):
#             self.__search_for_items(word)
#         for item in self.__items:
#             print(item.get_info())
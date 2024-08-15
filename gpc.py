# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# import time
# from item_cls import Item
#
#
# class GPC:
#     def __init__(self, driver: webdriver):
#         self.__driver = driver
#         self.__items = []
#
#     def __search_for_items(self, word: str):
#         self.__driver.get('https://gpc.ge/ka')
#         time.sleep(4)
#
#         search_box_xpath = "/html/body/div[1]/div[1]/div[3]/div/div/div[2]/form/input"
#
#         search_box = self.__driver.find_element(by=By.XPATH, value=search_box_xpath)
#         time.sleep(3)
#         search_box.send_keys(word)
#         search_box.send_keys(Keys.RETURN)
#
#         time.sleep(5)
#
#         wait = WebDriverWait(self.__driver, 10)
#
#         name_xpath = '/html/body/div[2]/div/div[3]/div[3]/div[2]/div/a/div[2]/div[1]'
#         country_xpath = '/html/body/div[2]/div/div[3]/div[3]/div[2]/div/a/div[2]/div[2]'
#         price_xpath = '/html/body/div[2]/div/div[3]/div[3]/div[2]/div/a/div[4]/div[1]/div[1]'
#         photo_xpath = '/html/body/div[2]/div/div[3]/div[3]/div[2]/div/a/div[1]/img'
#         link_xpath = '/html/body/div[2]/div/div[3]/div[3]/div[2]/div/a'
#         names = [name.text for name in wait.until(ec.presence_of_all_elements_located((By.XPATH, name_xpath)))]
#         countries = [country.text for country in
#                      wait.until(ec.presence_of_all_elements_located((By.XPATH, country_xpath)))]
#         prices = [float(price.text.replace('\n', '').replace('₾', '')) for price in
#                   wait.until(ec.presence_of_all_elements_located((By.XPATH, price_xpath)))]
#         photo_sources = [photo.get_attribute('src') for photo in
#                          wait.until(ec.presence_of_all_elements_located((By.XPATH, photo_xpath)))]
#         links = [elem.get_attribute('href') for elem in
#                  wait.until(ec.presence_of_all_elements_located((By.XPATH, link_xpath)))]
#
#         for i in range(len(prices)):
#             self.__items.append(Item(name=names[i], price=prices[i], photo_source=photo_sources[i], link=links[i], country=countries[i], pharmacy='GPC'))
#
#         # self.__driver.close()
#
#     def show_items(self, word):
#         if not len(self.__items):
#             self.__search_for_items(word)
#         for item in self.__items:
#             print(item.get_info())
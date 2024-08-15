# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# import time
# from item_cls import Item
#
#
# class Aversi:
#     def __init__(self, driver: webdriver):
#         self.__driver = driver
#         self.__items = []
#
#     def __search_for_items(self, word: str):
#         self.__driver.get('https://www.aversi.ge/')
#         time.sleep(2)
#
#         search_box_xpath = '/html/body/div[2]/div/section[2]/div/div/div[1]/div/form/div/div/div/input[1]'
#
#         search_box = self.__driver.find_element(by=By.XPATH, value=search_box_xpath)
#         search_box.send_keys(word)
#         search_box.send_keys(Keys.RETURN)
#         WebDriverWait(self.__driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
#         # Wait for the search results to load
#         wait = WebDriverWait(self.__driver, 10)
#
#         photo_xpath = '/html/body/div[2]/div/section[2]/div/div[5]/div/div/div/div[1]/a/img'
#         name_xpath = '/html/body/div[2]/div/section[2]/div/div[5]/div/div/div/div[2]/a/h5'
#         price_xpath = '/html/body/div[2]/div/section[2]/div/div[5]/div/div/div/div[2]/a/div[1]/ins/span'
#         country_xpath = '/html/body/div[2]/div/section[2]/div/div[5]/div/div/div/div[2]/a/div[2]/strong'
#         link_xpath = '/html/body/div[2]/div/section[2]/div/div[5]/div/div/div/div[1]/a'
#
#         photo_sources = [image.get_attribute('src') for image in
#                          wait.until(ec.presence_of_all_elements_located((By.XPATH, photo_xpath)))]
#         names = [name.text for name in wait.until(ec.presence_of_all_elements_located((By.XPATH, name_xpath)))]
#         prices = [float(price.text.replace(' ლარი', '')) for price in
#                   wait.until(ec.presence_of_all_elements_located((By.XPATH, price_xpath)))]
#         countries = [country.text for country in
#                      wait.until(ec.presence_of_all_elements_located((By.XPATH, country_xpath)))]
#         links = [elem.get_attribute('href') for elem in
#                  wait.until(ec.presence_of_all_elements_located((By.XPATH, link_xpath)))]
#
#         for i in range(len(prices)):
#             self.__items.append(Item(pharmacy='Aversi', name=names[i], price=prices[i], photo_source=photo_sources[i], link=links[i], country=countries[i]))
#
#         # self.__driver.close()
#
#     def show_items(self, word):
#         if not len(self.__items):
#             self.__search_for_items(word)
#         for item in self.__items:
#             print(item.get_info())

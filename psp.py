# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# import time
# from item_cls import Item
# import random
#
#
# class PSP:
#     def __init__(self, driver: webdriver):
#         self.__driver = driver
#         self.__items = []
#
#     def __scroll(self, max_scroll_time=30):
#         start_time = time.time()
#         total_height = self.__driver.execute_script("return document.body.scrollHeight")
#         scrolled = 0
#
#         while scrolled < total_height and time.time() - start_time < max_scroll_time:
#             # Scroll a random amount between 100 and 200 pixels
#             scroll_amount = random.randint(100, 200)
#             self.__driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
#             scrolled += scroll_amount
#
#             # Random pause between 0.5 and 1.5 seconds
#             time.sleep(random.uniform(0.5, 1.5))
#
#             # Occasionally pause for longer (simulating reading)
#             if random.random() < 0.1:  # 10% chance
#                 time.sleep(random.uniform(2, 4))
#
#             # Update total height in case of dynamic content
#             total_height = self.__driver.execute_script("return document.body.scrollHeight")
#
#         # Final scroll to bottom to ensure we've reached the end
#         self.__driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(1)
#
#     def __search_for_items(self, word: str):
#         self.__driver.get('https://psp.ge/')
#         time.sleep(2)
#
#         search_box_xpath = '/html/body/div[1]/header/div[2]/div[2]/div[1]/div[1]/div/div[1]/input'
#
#         search_box = self.__driver.find_element(by=By.XPATH, value=search_box_xpath)
#         search_box.send_keys(word)
#         search_box.send_keys(Keys.RETURN)
#         WebDriverWait(self.__driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, "body")))
#
#         self.__scroll()
#
#         wait = WebDriverWait(self.__driver, 10)
#
#         wait = WebDriverWait(self.__driver, 10)
#
#         photo_xpath = '/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/div/a/div[1]/div[1]/img'
#         name_xpath = '/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/div/a/div[2]'
#         price_xpath = '/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/div/a/div[3]/div[1]'
#         link_xpath = '/html/body/div[1]/div[1]/div/div/div/div[3]/div[2]/div/a'
#
#         prices = [float(price.text[:-1]) for price in
#                   wait.until(ec.presence_of_all_elements_located((By.XPATH, price_xpath)))]
#         photo_sources = [image.get_attribute('src') for image in
#                          wait.until(ec.presence_of_all_elements_located((By.XPATH, photo_xpath)))]
#         names = [name.text for name in wait.until(ec.presence_of_all_elements_located((By.XPATH, name_xpath)))]
#         links = [elem.get_attribute('href') for elem in
#                  wait.until(ec.presence_of_all_elements_located((By.XPATH, link_xpath)))]
#
#         for i in range(len(prices)):
#             self.__items.append(Item(pharmacy='PSP', country='-', name=names[i], price=prices[i], photo_source=photo_sources[i], link=links[i]))
#
#         # self.__driver.close()
#
#     def show_items(self, word):
#         if not len(self.__items):
#             self.__search_for_items(word)
#         for item in self.__items:
#             print(item.get_info())

# import requests
# import json
#
# from numpy.f2py.crackfortran import param_parse
# from urllib3 import request
#
# from main import Item
# import concurrent.futures
# import random
#
# class GPC:
#     def __init__(self):
#         self.api = 'https://gpcbackendprod.gepha.com/ka/web/medicaments/search
#         self.params = {
#             'input_text': 'PRODUCT',
#             'page': 'PAGE'
#         }
#         self.items: list[Item] = []
#
#     def fill_items(self, page_num):
#         self.params['page'] = str(page_num)
#         response = requests.post(self.api, params=self.params)
#         print(response.status_code)
#         data = response.json()['data']['search_result']
#         for med in data:
#             item = Item(pharmacy='Pharmadepot', name=med['name_sort'], price=float(med['price']), photo_source=med['image_url'],
#                          country=med['medicament_characteristic']['manufacturer_country_name'], old_price=med['initial_price'])
#             self.items.append(item)
#
#
#
#
#     def get_items(self, word: str):
#         self.params['input_text'] = word
#         self.params['page'] = '1'
#         page_count = int(requests.post(self.api, params=self.params).json()['data']['pagination']['total_pages'])
#         print(page_count)
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             executor.map(self.fill_items, range(1, page_count+1))
#
#
#
#
# gpc = GPC()
# gpc.get_items('ana')
#
# for i in gpc.items:
#     print(i.get_info())
#
# print('count', len(gpc.items), sep=' ->  ')
#
#
#
#
#
#
#
#
#
#
#
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.common.exceptions import NoSuchElementException, TimeoutException
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as ec
# # import time
# # from item_cls import Item
# # import concurrent.futures
# # import functools
# #
# #
# #
# # class Pharmacy:
# #     def __init__(self, search_url, photo_xpath,
# #                  name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
# #
# #         self.search_url: str = search_url
# #         self.photo_xpath = photo_xpath
# #         self.name_xpath = name_xpath
# #         self.price_xpath = price_xpath
# #         self.country_xpath = country_xpath
# #         self.link_xpath = link_xpath
# #         self.pharmacy = pharmacy
# #         self.items: list[Item] = []
# #         self.count = 0
# #
# #     def search_word(self, word, page_num, driver):
# #         driver.get(self.search_url.replace('replace_with_actual_word', word)
# #                         .replace('replace_with_actual_page_number', str(page_num)))
# #         time.sleep(3)
# #
# #     def get_names(self, wait):
# #         return [name.text for name in wait.until(ec.presence_of_all_elements_located((By.XPATH, self.name_xpath)))]
# #
# #     def get_countries(self, wait):
# #         return [country.text for country in
# #                 wait.until(ec.presence_of_all_elements_located((By.XPATH, self.country_xpath)))]
# #
# #     def get_photos(self, wait):
# #         return [photo.get_attribute('src') for photo in
# #                 wait.until(ec.presence_of_all_elements_located((By.XPATH, self.photo_xpath)))]
# #
# #     def get_links(self, wait):
# #         return [elem.get_attribute('href') for elem in
# #                 wait.until(ec.presence_of_all_elements_located((By.XPATH, self.link_xpath)))]
# #
# #     def get_prices(self, wait):
# #         return [price.text for price in wait.until(ec.presence_of_all_elements_located((By.XPATH, self.price_xpath)))]
# #
# #     def fill_items(self, names, prices, photo_sources, links, countries):
# #         for i in range(len(prices)):
# #             self.items.append(
# #                 Item(name=names[i], price=prices[i], photo_source=photo_sources[i],
# #                      pharmacy=self.pharmacy, link=links[i], country=countries[i]))
# #
# #
# #     def search_for_items(self, page_num, word: str):
# #         edge_options = webdriver.EdgeOptions()
# #         # edge_options.add_argument("--headless")
# #         # edge_options.add_argument("--disable-gpu")
# #         edge_options.add_experimental_option('detach', True)
# #         driver = webdriver.Edge(options=edge_options)
# #         wait = WebDriverWait(driver, 10)
# #         methods = [
# #             self.get_names,
# #             self.get_prices,
# #             self.get_photos,
# #             self.get_links,
# #             self.get_countries,
# #         ]
# #         def call_method(method):
# #             return method(wait)
# #
# #         try:
# #             self.search_word(word, page_num, driver)
# #             with concurrent.futures.ThreadPoolExecutor() as executor:
# #                 results = list(executor.map(call_method, methods))
# #             names, prices, photo_sources, links, countries = results
# #             self.fill_items(names, prices, photo_sources, links, countries)
# #             self.count += len(prices)
# #         except (TimeoutException, NoSuchElementException):
# #             driver.close()
# #         finally:
# #             driver.close()
# #
# #     def show_items(self, word):
# #         if not self.count:
# #             partial_search = functools.partial(self.search_for_items, word=word)
# #             with concurrent.futures.ThreadPoolExecutor() as executor:
# #                 executor.map(partial_search, range(1, 3))
# #         return [item.get_info() for item in self.items]
# #
# #
# #
# # def gpc_pharmadepot_price_decor(function):
# #     def wrapper(*args, **kwargs):
# #         lst = function(*args, **kwargs)
# #         res = [float(price.replace('\n', '').replace('₾', '')) for price in lst]
# #         return res
# #
# #     return wrapper
# #
# #
# # class GPC(Pharmacy):
# #     def __init__(self, search_url, photo_xpath,
# #                  name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
# #         super().__init__(search_url, photo_xpath,
# #                          name_xpath, price_xpath, country_xpath, link_xpath, pharmacy)
# #
# #
# #     @gpc_pharmadepot_price_decor
# #     def get_prices(self, wait):
# #         return super().get_prices(wait)
# #
# #
# # class Pharmadepot(Pharmacy):
# #     def __init__(self, search_url, photo_xpath,
# #                  name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
# #         super().__init__(search_url, photo_xpath,
# #                          name_xpath, price_xpath, country_xpath, link_xpath, pharmacy)
# #
# #
# #     @gpc_pharmadepot_price_decor
# #     def get_prices(self, wait):
# #         return super().get_prices(wait)
# #
# #
# # def psp_price_decor(function):
# #     def wrapper(*args, **kwargs):
# #         lst = function(*args, **kwargs)
# #         res = [float(price[:-1]) for price in lst]
# #         return res
# #
# #     return wrapper
# #
# #
# # class PSP(Pharmacy):
# #     def __init__(self, search_url, photo_xpath,
# #                  name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
# #         super().__init__(search_url, photo_xpath,
# #                          name_xpath, price_xpath, country_xpath, link_xpath, pharmacy)
# #
# #     @psp_price_decor
# #     def get_prices(self, wait):
# #         return super().get_prices(wait)
# #
# #     def __scroll(self, driver):
# #         total_height = driver.execute_script("return document.body.scrollHeight")
# #
# #         steps = 50
# #         scroll_time = 2
# #         time_per_step = scroll_time / steps
# #
# #         for i in range(steps):
# #             driver.execute_script(f"window.scrollTo(0, {(total_height / steps) * (i + 1)});")
# #             time.sleep(time_per_step)
# #
# #     def search_for_items(self, page_num, word: str):
# #         edge_options = webdriver.EdgeOptions()
# #         # edge_options.add_argument("--headless")
# #         # edge_options.add_argument("--disable-gpu")
# #         edge_options.add_experimental_option('detach', True)
# #         driver = webdriver.Edge(options=edge_options)
# #         wait = WebDriverWait(driver, 10)
# #         methods = [
# #             self.get_names,
# #             self.get_prices,
# #             self.get_photos,
# #             self.get_links,
# #         ]
# #
# #         def call_method(method):
# #             return method(wait)
# #
# #         try:
# #             self.search_word(word, page_num, driver)
# #             self.__scroll(driver)
# #             with concurrent.futures.ThreadPoolExecutor() as executor:
# #                 results = list(executor.map(call_method, methods))
# #             names, prices, photo_sources, links = results
# #             countries = ['-'] * len(names)
# #             self.fill_items(names, prices, photo_sources, links, countries)
# #             self.count += len(prices)
# #         except (TimeoutException, NoSuchElementException):
# #             driver.close()
# #         finally:
# #             driver.close()
# #
# #
# # def aversi_price_decor(function):
# #     def wrapper(*args, **kwargs):
# #         lst = function(*args, **kwargs)
# #         res = [float(price.replace(' ლარი', '')) for price in lst]
# #         return res
# #
# #     return wrapper
# #
# #
# # class Aversi(Pharmacy):
# #     def __init__(self, search_url, photo_xpath,
# #                  name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
# #         super().__init__(search_url, photo_xpath,
# #                          name_xpath, price_xpath, country_xpath, link_xpath, pharmacy)
# #
# #
# #     @aversi_price_decor
# #     def get_prices(self, wait):
# #         return super().get_prices(wait)
# #
# #     def get_countries(self, wait):
# #
# #         elems_xpath = '/html/body/div[2]/div/section[2]/div/div[5]/div/div'
# #         valid_paths = []
# #         i = 1
# #         while True:
# #             try:
# #                 curr_path = f'{elems_xpath}[{i}]'
# #                 elem = wait.until(ec.presence_of_element_located((By.XPATH, curr_path)))
# #             except:
# #                 break
# #             valid_paths.append(curr_path)
# #             i += 1
# #         countries = []
# #         for path in valid_paths:
# #             country = ''
# #             try:
# #                 country = wait.until(ec.presence_of_element_located((By.XPATH, f'{path}/div/div[2]/a/div[2]')))
# #                 countries.append(country.text.replace('ქვეყანა ', ''))
# #             except:
# #                 countries.append('-')
# #         return countries

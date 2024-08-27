from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import random
from item_cls import Item


class Pharmacy:
    def __init__(self, search_url, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
        edge_options = webdriver.EdgeOptions()
        # edge_options.add_argument("--headless")
        edge_options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(options=edge_options)
        self.search_url: str = search_url
        self.photo_xpath = photo_xpath
        self.name_xpath = name_xpath
        self.price_xpath = price_xpath
        self.country_xpath = country_xpath
        self.link_xpath = link_xpath
        self.pharmacy = pharmacy
        self.items: list[Item] = []
        self.count = 0

    def search_word(self, word, page_num):
        self.driver.get(self.search_url.replace('replace_with_actual_word', word)
                        .replace('replace_with_actual_page_number', str(page_num)))
        time.sleep(3)

    def get_names(self, wait):
        return [name.text for name in wait.until(ec.presence_of_all_elements_located((By.XPATH, self.name_xpath)))]

    def get_countries(self, wait):
        return [country.text for country in
                wait.until(ec.presence_of_all_elements_located((By.XPATH, self.country_xpath)))]

    def get_photos(self, wait):
        return [photo.get_attribute('src') for photo in
                wait.until(ec.presence_of_all_elements_located((By.XPATH, self.photo_xpath)))]

    def get_links(self, wait):
        return [elem.get_attribute('href') for elem in
                wait.until(ec.presence_of_all_elements_located((By.XPATH, self.link_xpath)))]

    def get_prices(self, wait):
        return [price.text for price in wait.until(ec.presence_of_all_elements_located((By.XPATH, self.price_xpath)))]

    def fill_items(self, names, prices, photo_sources, links, countries):
        print(len(names), len(countries), sep='----')
        for i in range(len(prices)):
            self.items.append(
                Item(name=names[i], price=prices[i], photo_source=photo_sources[i],
                     pharmacy=self.pharmacy, link=links[i], country=countries[i]))


    def search_for_items(self, word: str):
        wait = WebDriverWait(self.driver, 10)
        page_num = 1
        while True:
            try:
                self.search_word(word, page_num)
                names = self.get_names(wait)
                countries = self.get_countries(wait)  # problem with psp
                prices = self.get_prices(wait)
                photo_sources = self.get_photos(wait)
                links = self.get_links(wait)
                self.fill_items(names, prices, photo_sources, links, countries)
                self.count += len(prices)
            except (TimeoutException, NoSuchElementException):
                self.driver.close()
                break
            finally:
                page_num += 1

    def show_items(self, word):
        if not self.count:
            self.search_for_items(word)
        return [item.get_info() for item in self.items]


def gpc_pharmadepot_price_decor(function):
    def wrapper(*args, **kwargs):
        lst = function(*args, **kwargs)
        res = [float(price.replace('\n', '').replace('₾', '')) for price in lst]
        return res

    return wrapper


class GPC(Pharmacy):
    def __init__(self, search_url, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
        super().__init__(search_url, photo_xpath,
                         name_xpath, price_xpath, country_xpath, link_xpath, pharmacy)


    @gpc_pharmadepot_price_decor
    def get_prices(self, wait):
        return super().get_prices(wait)


class Pharmadepot(Pharmacy):
    def __init__(self, search_url, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
        super().__init__(search_url, photo_xpath,
                         name_xpath, price_xpath, country_xpath, link_xpath, pharmacy)


    @gpc_pharmadepot_price_decor
    def get_prices(self, wait):
        return super().get_prices(wait)


def psp_price_decor(function):
    def wrapper(*args, **kwargs):
        lst = function(*args, **kwargs)
        res = [float(price[:-1]) for price in lst]
        return res

    return wrapper


class PSP(Pharmacy):
    def __init__(self, search_url, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
        super().__init__(search_url, photo_xpath,
                         name_xpath, price_xpath, country_xpath, link_xpath, pharmacy)

    @psp_price_decor
    def get_prices(self, wait):
        return super().get_prices(wait)

    def __scroll(self, max_scroll_time=30):
        start_time = time.time()
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        scrolled = 0

        while scrolled < total_height and time.time() - start_time < max_scroll_time:
            # Scroll a random amount between 100 and 200 pixels
            scroll_amount = random.randint(100, 200)
            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            scrolled += scroll_amount
            total_height = self.driver.execute_script("return document.body.scrollHeight")

        # Final scroll to bottom to ensure we've reached the end
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def search_for_items(self, word: str):
        wait = WebDriverWait(self.driver, 10)
        page_num = 1
        while True:
            try:
                self.search_word(word, page_num)
                self.__scroll(4)
                names = self.get_names(wait)
                countries = ['-'] * len(names)
                prices = self.get_prices(wait)
                photo_sources = self.get_photos(wait)
                links = self.get_links(wait)
                self.fill_items(names, prices, photo_sources, links, countries)
                self.count += len(prices)
            except (TimeoutException, NoSuchElementException):
                self.driver.close()
                break
            finally:
                page_num += 1


def aversi_price_decor(function):
    def wrapper(*args, **kwargs):
        lst = function(*args, **kwargs)
        res = [float(price.replace(' ლარი', '')) for price in lst]
        return res

    return wrapper


class Aversi(Pharmacy):
    def __init__(self, search_url, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath, pharmacy):
        super().__init__(search_url, photo_xpath,
                         name_xpath, price_xpath, country_xpath, link_xpath, pharmacy)


    @aversi_price_decor
    def get_prices(self, wait):
        return super().get_prices(wait)

    def get_countries(self, wait):

        elems_xpath = '/html/body/div[2]/div/section[2]/div/div[5]/div/div'
        valid_paths = []
        i = 1
        while True:
            try:
                curr_path = f'{elems_xpath}[{i}]'
                elem = self.driver.find_element(By.XPATH, curr_path)
            except:
                break
            valid_paths.append(curr_path)
            i += 1
        countries = []
        for path in valid_paths:
            country = ''
            try:
                country = self.driver.find_element(By.XPATH, f'{path}/div/div[2]/a/div[2]')
                countries.append(country.text.replace('ქვეყანა ', ''))
            except:
                countries.append('-')
        return countries

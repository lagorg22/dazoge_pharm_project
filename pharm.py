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
    def __init__(self, website, search_box_xpath, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath):
        edge_options = webdriver.EdgeOptions()
        # edge_options.add_argument("--headless")
        # edge_options.add_argument("--disable-gpu")
        edge_options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(options=edge_options)
        self.website = website
        self.search_box_xpath = search_box_xpath
        self.photo_xpath = photo_xpath
        self.name_xpath = name_xpath
        self.price_xpath = price_xpath
        self.country_xpath = country_xpath
        self.link_xpath = link_xpath
        self.items = []
        self.count = 0

    def search_word(self, word):
        search_box = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, self.search_box_xpath)))
        search_box.send_keys(word)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

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
        for i in range(len(prices)):
            self.items.append(
                Item(name=names[i], price=prices[i], photo_source=photo_sources[i],
                     pharmacy='-', link=links[i], country=countries[i]))

    def go_to_next_page(self):
        try:
            next_button = self.driver.find_element(by=By.CSS_SELECTOR, value='button[title="შემდეგი"]')
        except NoSuchElementException:
            self.driver.close()
            return False
        self.driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)
        return True

    def search_for_items(self, word: str):
        self.driver.get(self.website)

        time.sleep(2)

        self.search_word(word)

        wait = WebDriverWait(self.driver, 10)
        while True:
            names = self.get_names(wait)
            countries = self.get_countries(wait)  # problem with psp
            prices = self.get_prices(wait)
            photo_sources = self.get_photos(wait)
            links = self.get_links(wait)
            self.fill_items(names, prices, photo_sources, links, countries)
            if not self.go_to_next_page():
                break
        self.count += len(prices)

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
    def __init__(self, website, search_box_xpath, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath):
        super().__init__(website, search_box_xpath, photo_xpath,
                         name_xpath, price_xpath, country_xpath, link_xpath)
        self.__pharmacy = 'GPC'

    def fill_items(self, names, prices, photo_sources, links, countries):
        for i in range(len(prices)):
            self.items.append(
                Item(name=names[i], price=prices[i], photo_source=photo_sources[i],
                     pharmacy=self.__pharmacy, link=links[i], country=countries[i]))

    @gpc_pharmadepot_price_decor
    def get_prices(self, wait):
        return super().get_prices(wait)


class Pharmadepot(Pharmacy):
    def __init__(self, website, search_box_xpath, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath):
        super().__init__(website, search_box_xpath, photo_xpath,
                         name_xpath, price_xpath, country_xpath, link_xpath)
        self.__pharmacy = 'Pharmadepot'

    def fill_items(self, names, prices, photo_sources, links, countries):
        for i in range(len(prices)):
            self.items.append(
                Item(name=names[i], price=prices[i], photo_source=photo_sources[i],
                     pharmacy=self.__pharmacy, link=links[i], country=countries[i]))

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
    def __init__(self, website, search_box_xpath, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath):
        super().__init__(website, search_box_xpath, photo_xpath,
                         name_xpath, price_xpath, country_xpath, link_xpath)
        self.__pharmacy = 'PSP'

    def fill_items(self, names, prices, photo_sources, links, countries):
        for i in range(len(prices)):
            self.items.append(
                Item(name=names[i], price=prices[i], photo_source=photo_sources[i],
                     pharmacy=self.__pharmacy, link=links[i], country='-'))

    def get_countries(self, wait):
        return ['-' * self.count]

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
        self.driver.get(self.website)

        time.sleep(2)

        self.search_word(word)

        wait = WebDriverWait(self.driver, 10)
        max_page = 1
        try:
            max_page = max([int(num.text) for num in WebDriverWait(self.driver, 10).until(
                ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'li[class="number"]')))])
        except TimeoutException:
            pass

        for i in range(1, max_page + 1):
            i = str(i)
            next_page = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, f"//li[text()={i}]")))
            self.driver.execute_script("arguments[0].click();", next_page)
            time.sleep(2)
            self.__scroll(2)

            names = self.get_names(wait)
            countries = self.get_countries(wait)  # problem with psp
            prices = self.get_prices(wait)
            photo_sources = self.get_photos(wait)
            links = self.get_links(wait)
            self.fill_items(names, prices, photo_sources, links, countries)
            self.count += len(prices)
        self.driver.close()


def aversi_price_decor(function):
    def wrapper(*args, **kwargs):
        lst = function(*args, **kwargs)
        res = [float(price.replace(' ლარი', '')) for price in lst]
        return res

    return wrapper


class Aversi(Pharmacy):
    def __init__(self, website, search_box_xpath, photo_xpath,
                 name_xpath, price_xpath, country_xpath, link_xpath):
        super().__init__(website, search_box_xpath, photo_xpath,
                         name_xpath, price_xpath, country_xpath, link_xpath)
        self.__pharmacy = 'Aversi'

    def fill_items(self, names, prices, photo_sources, links, countries):
        for i in range(len(prices)):
            self.items.append(
                Item(name=names[i], price=prices[i], photo_source=photo_sources[i],
                     pharmacy=self.__pharmacy, link=links[i], country=countries[i]))

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

    def go_to_next_page(self):
        try:
            next_button = self.driver.find_element(by=By.CSS_SELECTOR, value='a[rel="next"]')
        except NoSuchElementException:
            self.driver.close()
            return False
        self.driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)
        return True

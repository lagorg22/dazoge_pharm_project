import requests
import json

class Item:
    def __init__(self, pharmacy: str, name: str, price: float, photo_source: str, country: str, old_price):
        self.__name = name
        self.__price = price
        self.__old_price = old_price
        self.__photo_source = photo_source
        self.__country = country
        self.__pharmacy = pharmacy

    def get_pharmacy(self):
        return self.__pharmacy

    def get_country(self):
        return self.__country

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_photo_source(self):
        return self.__photo_source

    def get_old_price(self):
        return self.__old_price

    def get_info(self):
        return {'Pharmacy': self.get_pharmacy(),
                'Name': self.get_name(),
                'Country': self.get_country(),
                'Price': self.get_price(),
                'Old Price': self.get_old_price(),
                'Photo Source': self.get_photo_source(),
                }

# params = {"input_text": "დიაზეპამი", "page": "1"}
#
# url = 'https://gpcbackendprod.gepha.com/ka/web/medicaments/search'
# response = requests.post(url, params=params)
# print(response.json()['data']['search_result'][0])

# params = {"input_text": "panadol", "page": "1"}
#
# url = 'https://pharmbackend-prod.gepha.com/ka/web/medicaments/search'
# response = requests.post(url, params=params)
# print(response.json()['data']['search_result'][0])

# params = {"page": "1", "currentPage": "1", "search": "ana", "query": "ana"}
#
# url = 'https://psp.ge/product/list'
# response = requests.get(url, params=params)
# print(response.json()['data']['items'][0])
#
# params = {'match': 'all',
#           'search_performed': 'Y',
#           'q': 'საფენი',
#           'dispatch': 'products.search',
#           'page': '8',
#           'sl': 'ka',
#           'is_ajax':'1'}
#
# url = 'https://shop.aversi.ge/index.php'
# response = requests.get(url, params=params)
# print(response.json()['cp_gtm']['view_products'])

pharm_data = {
    'GPC': {
        'url': 'https://gpcbackendprod.gepha.com/ka/web/medicaments/search',
        'params': {
            "input_text": "TEXT",
            "page": "PAGE"
        }
    },
    'Pharmadepot': {
        'url': 'https://pharmbackend-prod.gepha.com/ka/web/medicaments/search',
        'params': {
            "input_text": "TEXT",
            "page": "PAGE"
        }
    },
    'PSP': {
        'url' : 'https://psp.ge/product/list',
        'params': {
            "page": "PAGE",
            "currentPage": "PAGE",
            "search": "TEXT",
            "query": "TEXT"
        }
    },
    'Aversi': {
        'url': 'https://shop.aversi.ge/index.php',
        'params': {

            'match': 'all',
            'search_performed': 'Y',
            'q': 'TEXT',
            'dispatch': 'products.search',
            'page': 'PAGE',
            'sl': 'ka',
            'is_ajax':'1'
        }
    }
}
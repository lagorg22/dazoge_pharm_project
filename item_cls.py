class Item:
    def __init__(self, pharmacy: str, name: str, price: float, photo_source: str, link: str,  country: str):
        self.__name = name
        self.__price = price
        self.__photo_source = photo_source
        self.__link = link
        self.__country = country
        self.__pharmacy = pharmacy

    def get_pharmacy(self):
        return self.__pharmacy

    def get_country(self):
        return self.__country

    def get_link(self):
        return self.__link

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_photo_source(self):
        return self.__photo_source

    def get_info(self):
        return {'Pharmacy': self.get_pharmacy(),
                'Name': self.get_name(),
                'Country': self.get_country(),
                'Price': self.get_price(),
                'Photo Source': self.get_photo_source(),
                'Link': self.get_link()}


# class PharmadepotItem(Item):
#     def __init__(self, name, price, photo_source, link,  country):
#         super().__init__(name, price, photo_source, link, country)
#         self.__pharmacy = 'Pharmadepot'
#
#     def get_country(self):
#         return self.__country
#
#     def get_pharmacy(self):
#         return self.__pharmacy
#
#     def get_info(self):
#         return (f'Pharmacy: {self.get_pharmacy()} \n'
#                 f'{super().get_info()}')
#
#
# class GPCItem(Item):
#     def __init__(self, name, price, photo_source, link, country):
#         super().__init__(name, price, photo_source, link, country)
#         self.__pharmacy = 'GPC'
#
#     def get_country(self):
#         return self.__country
#
#     def get_pharmacy(self):
#         return self.__pharmacy
#
#     def get_info(self):
#         return (f'Pharmacy: {self.get_pharmacy()} \n'
#                 f'{super().get_info()}')
#
#
# class PSPItem(Item):
#     def __init__(self, name, price, photo_source, link, country='-'):
#         super().__init__(name, price, photo_source, link, country)
#         self.__pharmacy = 'PSP'
#
#     def get_pharmacy(self):
#         return self.__pharmacy
#
#     def get_info(self):
#         return (f'Pharmacy: {self.get_pharmacy()} \n'
#                 f'{super().get_info()}')
#
#
# class AversiItem(Item):
#     def __init__(self, name, price, photo_source, link, country):
#         super().__init__(name, price, photo_source, link, country)
#         self.__country = country
#         self.__pharmacy = 'Aversi'
#
#     def get_country(self):
#         return self.__country
#
#     def get_pharmacy(self):
#         return self.__pharmacy
#
#     def get_info(self):
#         return (f'Pharmacy: {self.get_pharmacy()} \n'
#                 f'{super().get_info()}')
#
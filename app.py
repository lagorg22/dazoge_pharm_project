import json
from pharm import GPC, PSP, Pharmadepot, Aversi
import pandas as pd

with open('paths.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def get_inputs(pharmacy):
    d = data[pharmacy]
    return [d['website'], d['search_box_xpath'], d['photo_xpath'], d['name_xpath'], d['price_xpath'], d['country_xpath'], d['link_xpath']]


word = 'ana'
# ps = PSP(*get_inputs('psp'))
# ps.show_items(word)
# ph = Pharmadepot(*get_inputs('pharmadepot'))
# ph.show_items(word)
# av = Aversi(*get_inputs('aversi'))
# av.show_items(word)
gp = GPC(*get_inputs('gpc'))
# print(gp.show_items(word))
# df = pd.DataFrame(columns=['Pharmacy', 'Name', 'Country', 'Price', 'Photo Source', 'Link'])
# for item_dict in gp.show_items(word):
#     df.loc[len(df)] = item_dict
#
# # print(df)
#
# df.to_excel('test1.xlsx')



import json
from pharm import GPC, PSP, Pharmadepot, Aversi
from flask import Flask, render_template, request
import concurrent.futures

# import pandas as pd

with open('paths.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def get_inputs(pharmacy):
    d = data[pharmacy]
    return [d['search_url'], d['photo_xpath'], d['name_xpath'], d['price_xpath'], d['country_xpath'], d['link_xpath']]

word = 'ანალგინი'

objects = ['GPC', 'PSP', 'Pharmadepot', 'Aversi']
res = []
def fun(s):
    o = globals()[s](*get_inputs(s.lower()), pharmacy=s)
    res.extend(o.show_items(word))


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(fun, objects)

print(res)

# gp = GPC(*get_inputs('gpc'), pharmacy='GPC')
# gpc_infos = gp.show_items(word)
#
# ps = PSP(*get_inputs('psp'), pharmacy='PSP')
# ps_infos = ps.show_items(word)
#
# ph = Pharmadepot(*get_inputs('pharmadepot'), pharmacy='Pharmadepot')
# ph_infos = ph.show_items(word)
#
# av = Aversi(*get_inputs('aversi'), pharmacy='Aversi')
# av_infos = av.show_items(word)
#
# items_infos = gpc_infos + av_infos + ph_infos + ps_infos
#
# items_infos = sorted(items_infos, key=lambda x: x['Price'])
#
# print(items_infos)


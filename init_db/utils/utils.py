import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import csv
import numpy as np
import concurrent.futures

from requests.models import parse_url
from utils import list_needed
# from backward_app.utils import parse_page_functions #Personnal function

def immoweb_parse(url):
    page = requests.get(url)
    if page.status_code == 200:
        soup    = BeautifulSoup(page.content, "lxml")
        script  = soup.find_all("script", type="text/javascript")
        raw     = (
                script[2]
                .decode_contents()
                .lstrip("\nwindow.classified = )")
                .rstrip(";\n        ")
                )
        # print(raw)
        dictionary = flatten_json(json.loads(raw))
        if dictionary['price_type'] != 'residential_sale': 
            return None
        if dictionary["transaction_sale_price"] == None:
            return None
        return dictionary
    else:
        return None

def flatten_json(json_raw):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(json_raw)
    return out

def parsing_page(index):
    key_words = list_needed.key_words
    df = pd.read_csv("../data_set/clean_url_202105261026.csv")
    max_iteration = len(df)

    with open("../data_set/clean_url_202105261026.csv", "r") as file:
        csv_reader = csv.reader(file)
        csv_list= list(csv_reader)
        dic_temp = {}

        for i in range(index, max_iteration, 20):
            url = csv_list[i]
            dico_json = immoweb_parse(url[0])
            if dico_json == None:
                continue

            for key_word in key_words:
                try:
                    dic_temp[key_word] = dico_json[key_word]
                except:
                    dic_temp[key_word] = None           

            with open("../data_set/db_immoweb.csv", "a+") as file:
                csv_writer = csv.DictWriter(file, fieldnames = key_words)
                csv_writer.writerow(dic_temp)

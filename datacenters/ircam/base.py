# Grandma, grandma never die
# I shall love you all the way
# I will make you a dictionay
# To conserve all your memory

import requests
import json
import codecs
import pandas as pd
import numpy as np


class Ircam:
    def __init__(self):
        self.word_api = 'https://tal.ircam.ma/dglai/service/simple_search_fr_ar.php?term={}&lang=fr'
        self.class_api = 'https://tal.ircam.ma/dglai/service/classegs.php?lexie={}'

    @staticmethod
    def _get_data(endpoint):
        r = requests.get(endpoint)
        decoded_data = codecs.decode(r.text.encode(), 'utf-8-sig')
        data = json.loads(decoded_data)
        return data

    @staticmethod
    def _format_data(data):
        data = data['lexie']
        columns = ['ircam_id', 'amz', 'fr']
        df = pd.DataFrame(columns=columns)
        if data:
            for el in data:
                df = df.append(
                    pd.Series(
                    [
                        el['id'],
                        el['api'],
                        el['traductionFr'],        
                    ],
                    index=columns
                    ),
                    ignore_index=True
                )
        return df

    @staticmethod
    def eng_class(wclass):
        dico = {
            'verbe': 'verb',
            'nom': 'noun',
            'interjection': 'interjection',
            'conjonction': 'conjunction',
            'adverbe': 'adverb',
            'particule': 'determiner',
        }

        if wclass in dico.keys():
            return dico[wclass]
        return wclass

    def get_word_class_df(self, ircam_id):
        endpoint = self.class_api.format(ircam_id)
        data = self._get_data(endpoint)
        data = data['lexie']
        columns = ['ircam_id', 'class', 'sub_class']
        df = pd.DataFrame(columns=columns)
        if data:
            for el in data:
                wclass = self.eng_class(el['classe'])
                sclass = el['sclasse'],
                if (sclass=='(;,)'):
                    sclass = np.nan
                    print(sclass)
                df = df.append(
                    pd.Series(
                    [
                        ircam_id,   
                        wclass,
                        sclass,
                    ],
                    index=columns
                    ),
                    ignore_index=True
                )
        return df

    def get_word_df(self, word, lang='fr'):
        if (lang=='fr'):
            endpoint = self.word_api.format(word)
            data = self._get_data(endpoint)
            df = self._format_data(data)
            return df

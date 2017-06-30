import json
import requests # need this. pip install requests
import pprint
import sys


# using https://developer.edamam.com/ free account for access to recipes

APIkey = {'app_id': '9792fcf6','app_key': 'e3ee438479c99b54df6cba3be90a6359', 'q': ''}
# q is name of recipe, app id and app key are api keys
# get your own key or use mine


def query(item_name):
    APIkey['q'] = item_name #set input to q(recipename) in query to website
    r = requests.get('https://api.edamam.com/search',params=APIkey)
    json_obj = r.json() # store request get into obj to use
    return json_obj['hits'][0]['recipe']  # can access hits but not specify other field


def get_calories(hit_obj):
    return int(hit_obj['calories'])


def get_label(hit_obj):
    return str(hit_obj['label'])


def get_ingredients(hit_obj):
    d = []
    for item in hit_obj['ingredientLines']:
        d.append(item)
    return d


readable = query(input())
print('Calories: ',get_calories(readable))
print(get_label(readable))
print('\n'.join('{}: {}'.format(*k) for k in enumerate(get_ingredients(readable))))
# pp = pprint.PrettyPrinter(indent=4) # make pprint object with cute organzied output
# pp.pprint(query(input())) #type in a recipe name. returns all json related to it.
# sys.exit()



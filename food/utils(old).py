import requests
import re
import json
from food.models import Categorie

""" Open Food Facts API function """
def get_product(search):
    """ Get some substitute """
    # Download the the product list from the search word
    search = search.capitalize()
    payload = {'json': '1', 'page_size': '20', 'search_simple': '1'}
    result_url = requests.get(
        'https://fr.openfoodfacts.org/cgi/search.pl?search_terms='+ search, params = payload)
    data = result_url.json()
    if data["count"] >= 1:
        # Extract the categorie list and nutrition grade from the product list
        categorie = []
        for product_count in range(int(data["page_size"])):
            categorie_list = data["products"][product_count]["categories_tags"]
            categorie = [item[3:] for item in categorie_list if item[:2] == "fr"]
            if len(categorie) >= 1:
                nutrition_grade = data["products"][product_count]["nutrition_grades_tags"]
                result = categorie, nutrition_grade
                print("categorie: " + str(categorie) + " nut: " + str(nutrition_grade))
                return result
    else:
        # No result
        return None

def get_result(categorie, nutrition_grade):
    """ Get the product list result form OpenFood Facts """
    cat = categorie[(len(categorie)-1)]
    try:
        cat_url = cat.replace('-', ' ')
        print('cat_match_try: ' + str(cat_url))
        categorie_match = Categorie.objects.get(categorie_name=cat_url.capitalize())
    except:
        print('cat_match_except: ' + str(cat_url))
        categorie_match = Categorie.objects.get(categorie_name=cat_url.capitalize())[:1]
    data_url = requests.get(categorie_match.categorie_url + '.json')
    data = data_url.json()
    json_lenght = data["count"]
    if json_lenght > 20:
        json_lenght = 20
    product = []
    item_count = 0
    for rank in range(0, json_lenght):
        if "nutrition_grades_tags" in data["products"][rank]:
            if data["products"][rank]["nutrition_grades_tags"] <= nutrition_grade:
                if "image_front_url" in data["products"][rank]:
                    temp_list = []
                    temp_list.append(data["products"][rank]["image_front_url"])
                    temp_list.append(data["products"][rank]["nutrition_grades_tags"][0])
                    temp_list.append(data["products"][rank]["product_name"])
                    product.append(temp_list)
                    item_count += 1
                    if item_count == 6:
                        break
                else:
                    continue
            else:
                continue
        else:
            continue
    return json.dumps(product)
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as url
import multiprocessing
import pandas as pd
import os
import sys


class Recipe:
    title = None
    rating = None
    personal_rating = []
    calories = None
    sodium = None
    fat = None
    protein = None

    def __init__(self, page):
        print('attempting to build from: ' + page)
        try:
            self.build_recipe(bs(url(page), 'html.parser'))
        except Exception as x:
            print('Could not build from %s, %s' % (page, x))

    def build_recipe(self, page):
        self.title = self.get_title(page)
        self.rating = self.get_rating(page)
        self.calories = self.get_calories(page)
        self.sodium = self.get_sodium(page)
        self.fat = self.get_fat(page)
        self.protein = self.get_protein(page)
        self.personal_rating = self.get_personal_rating(page)

    @staticmethod
    def get_title(page):
        return page.find('h1', {'itemprop': 'name'}).text

    @staticmethod
    def get_rating(page):
        try:
            return float(page.find_all('span', {'class': 'rating'})[-1].text.split('/')[0]) + 1
        except:
            return None

    @staticmethod
    def get_calories(page):
        try:
            return float(page.find('span', {'class': 'nutri-data', 'itemprop': 'calories'}).text)
        except:
            return None

    @staticmethod
    def get_sodium(page):
        try:
            return float(page.find('span', {'class': 'nutri-data', 'itemprop': 'sodiumContent'}).text.split(' ')[0])
        except:
            return None

    @staticmethod
    def get_fat(page):
        try:
            return float(page.find('span', {'class': 'nutri-data', 'itemprop': 'fatContent'}).text.split(' ')[0])
        except:
            return None

    @staticmethod
    def get_protein(page):
        try:
            return float(page.find('span', {'class': 'nutri-data', 'itemprop': 'proteinContent'}).text.split(' ')[0])
        except:
            return None

    @staticmethod
    def get_personal_rating(page):
        try:
            p_ratings = page.findAll('img', {'class': 'fork-rating'})
            p_persons = page.find_all('span', {'class': 'credit'})
            p_r = []
            for i in range(len(p_ratings)):
                temp = [p_persons[i].text.split('/')[0], int(p_ratings[i]['src'].split('/')[-1].split('_')[0]) + 1]
                p_r.append(temp)
            return p_r
        except:
            return None


def scraping():
    script_dir = os.path.abspath(os.path.dirname(sys.argv[0]) or '.')
    nutrition_info_path = os.path.join(script_dir, './resource/meal_problem/nutrition_info.csv')
    final_rating_data_path = os.path.join(script_dir, './resource/meal_problem/final_rating_data.csv')

    all_url = [
        'https://www.epicurious.com/recipes-menus/what-to-cook-this-weekend-february-22-24-gallery',
        'https://www.epicurious.com/recipes-menus/what-to-cook-this-weekend-february-8-10-gallery',
        "https://www.epicurious.com/ingredients/acorn-delicata-kabocha-spaghetti-squash-winter-recipes-gallery",
        'https://www.epicurious.com/recipes-menus/easy-dinner-recipes-for-cook90-gallery',
        'https://www.epicurious.com/recipes-menus/our-favorite-cook90-lunches-gallery',
        'https://www.epicurious.com/recipes-menus/make-ahead-weeknight-dinners-stew-soup-freezer-casserole-quick-easy'
        '-recipes-gallery',
    ]

    ep_urls = set()
    for i in all_url:
        initializer = url(i)
        res = bs(initializer.read(), "html.parser")
        for div in res.findAll('div', {'class': 'gallery-slide-caption__dek-container'}):
            ep_urls.update([div.find('a')['href']])

    p = multiprocessing.Pool(4)
    output = p.map(Recipe, ep_urls)
    ar = []
    for i in output:
        ar.append(i.__dict__)
    df = pd.DataFrame(ar)
    df = df.dropna(axis=0)
    df = df[df['personal_rating'].map(len) > 9]
    df.to_csv(nutrition_info_path)

    p_r = pd.DataFrame(columns=['title', 'user', 'rating'])
    count = 0
    for i in range(df.shape[0]):
        for j in df.iloc[i, 6]:
            p_r.loc[count] = [df.iloc[i, 0], j[0], j[1]]
            count += 1

    user_reviews2 = p_r['user'].value_counts()[p_r['user'].value_counts() > 0].index
    trun_recipes_user_review = p_r[p_r['user'].isin(user_reviews2)]
    trun_recipes_user_review = trun_recipes_user_review.drop_duplicates(['user', 'title'])
    trun_recipes_user_review_matrix = trun_recipes_user_review.pivot(index='user', columns='title', values='rating')
    final_rating_data = pd.DataFrame(columns=trun_recipes_user_review_matrix.columns)
    for i in range(trun_recipes_user_review_matrix.shape[0] // 50):
        temp = trun_recipes_user_review_matrix.iloc[50 * i:50 * i + 50].mean(skipna=True, axis=0)
        temp.name = 'user' + str(i)
        final_rating_data.loc[i] = temp

    final_rating_data.to_csv(final_rating_data_path)

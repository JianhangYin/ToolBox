from fancyimpute import SoftImpute
import numpy as np
import pandas as pd

'''
filtering:
We will add the two people into our rating database (n)
Then do the matrix completion with the new data
Finally, return the (n + 2) completion matrix
Input:
1. food_list: the five random recipes(list of string)
2. food_a: the rate for person A(list of int)
3. food_b: the rate for person B(list of int)
Output:
{
    'Monday': ['A', 'recipe A'],
    'Tuesday': ['B', 'recipe B'],
    'Wednesday': ['B', 'recipe C'],
    'Thursday': ['A', 'recipe B'],
    'Friday': ['A', 'recipe D'],
}
'''


def filtering(food_list, food_a, food_b):
    df = pd.read_csv('./resource/meal_problem/final_rating_data.csv')
    df = df.iloc[:, 1:]
    df = df.append(build_new_row(food_list, food_a), ignore_index=True)
    df = df.append(build_new_row(food_list, food_b), ignore_index=True)
    df_numeric = df.select_dtypes(include=[np.float]).to_numpy()
    df_new = pd.DataFrame(SoftImpute().fit_transform(df_numeric))
    df_new.columns = df.columns
    return df_new


def build_new_row(food_list, food_rate):
    dic = {}
    for i in range(len(food_list)):
        dic[food_list[i]] = food_rate[i]
    return dic


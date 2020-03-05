import pandas as pd


def getting():
    df = pd.read_csv('./resource/meal_problem/nutrition_info.csv')
    df = df.loc[:, ['title']].sample(5)
    return df.values.tolist()

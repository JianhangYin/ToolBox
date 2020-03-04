from fancyimpute import SoftImpute
import numpy as np
import pandas as pd


def filtering():
    df = pd.read_csv('./resource/meal_problem/final_rating_data.csv')
    df_numeric = df.select_dtypes(include=[np.float]).to_numpy()
    df_new = pd.DataFrame(SoftImpute().fit_transform(df_numeric))
    df_new.columns = df.columns[1:]
    return df_new

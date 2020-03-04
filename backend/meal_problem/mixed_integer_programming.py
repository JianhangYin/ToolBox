from docplex.mp.model import Model
import backend.meal_problem.collaborative_filtering as cf
import pandas as pd

'''
Programming:
Input:
1. number: the number of recipes(int)
2. time: time available for two people(list of list)
3. budget: the budget(int)
4. name_list: the list of two people's names(list of string)
Output:
{
    'Monday': ['A', 'recipe A'],
    'Tuesday': ['B', 'recipe B'],
    'Wednesday': ['B', 'recipe C'],
    'Thursday': ['A', 'recipe B'],
    'Friday': ['A', 'recipe D'],
}
'''


def programming(number, time, budget, name_list):
    df = cf.filtering()
    dfn = pd.read_csv('./resource/meal_problem/nutrition_info.csv')
    recipe_list = df.columns.tolist()
    recipe_len = number

    MnM = Model(name='Meal Planning for the New Millennium')
    x = {(i, t, k): MnM.binary_var(name='x_{0}_{1}_{2}'.format(i, t, k)) for i in range(2) for t in range(5) for k in
         range(recipe_len)}
    w = MnM.continuous_var(name='w', lb=0)

    # recipe matrix
    K = recipe_len
    T = time

    # rating for user 0 and user 1
    rating = df.iloc[0:2, 0:K].values.tolist()

    calories = dfn['calories'][:number]
    protein = dfn['protein'][:number]
    fat = dfn['fat'][:number]
    sodium = dfn['sodium'][:number]
    price = [
        06.36, 5.46, 17.46, 11.06, 11.24, 5.71, 3.44, 8.35, 13.86,
        11.20, 11.85, 12.77, 8.24, 8.13, 11.92, 10.57, 11.47, 11.82,
        05.77, 10.92, 12.88, 4.87, 8.19, 12.13, 14.67, 9.05, 9.25,
        14.09, 10.11, 9.62, 10.1, 10.64, 5.84, 8.89, 6.8, 11.8,
        13.23, 9.09, 10.11, 5.46, 9.16, 10.96, 6.22, 12.79, 11.91,
        13.43, 11.29, 14.42, 11.88, 8.02, 11.77, 6.98, 8.1, 10.88,
        13.6, 13.32, 6.59, 5.07, 10.43, 15.79, 5.07, 5.66, 10.14,
        7.89, 7.87, 11.39, 5.14, 9.71, 10.6, 9.89, 9.15, 7.22,
        3.74, 7.47, 10.34, 14.44, 11.76, 10.93, 7.91, 13.37, 10.24,
        14.35, 11.0, 14.6, 13.55, 8.06, 9.04, 9.61, 8.11, 10.07,
        11.7, 13.05, 12.92, 9.81, 7.83, 9.36, 10.68, 9.43, 9.46,
        9.58, 12.63, 7.34, 4.53, 7.51, 9.6, 4.3, 12.75, 12.7,
        15.73, 2.43, 2.51, 8.45, 8.76, 7.34, 12.84
    ]

    tau = [
        42, 32, 34, 40, 44, 29, 54, 45, 40, 28, 35, 42, 53, 38, 44, 60, 20,
        50, 28, 49, 38, 30, 45, 36, 62, 45, 46, 36, 58, 47, 39, 41, 27, 41,
        58, 38, 31, 46, 66, 53, 48, 25, 34, 34, 36, 48, 39, 27, 47, 36, 66,
        49, 46, 37, 34, 31, 54, 39, 46, 48, 42, 46, 36, 39, 39, 31, 44, 41,
        34, 25, 48, 48, 40, 42, 46, 46, 42, 27, 39, 37, 34, 33, 50, 38, 30,
        27, 48, 32, 29, 39, 38, 44, 37, 35, 40, 24, 33, 37, 49, 53, 41, 38,
        20, 28, 56, 41, 50, 33, 38, 27, 25, 69, 64, 31, 56
    ]
    # lower(1) and upper(2) bound of nutrient
    c_bound = [2700, 3600]
    p_bound = [140, 200]
    f_bound = [150, 250]
    s_bound = [2400, 3000]
    B = budget  # budget

    # parameter for objective
    alpha = 0.1
    # five meals constraints, one meal per day
    for t in range(5):
        MnM.add_constraint(MnM.sum(x[i, t, k] for i in range(2) for k in range(K)) == 1,
                           ctname='subject to five_meals_total')

    # nutrition lower bound
    MnM.add_constraint(
        MnM.sum(calories[k] * x[i, t, k] for i in range(2) for t in range(5) for k in range(K)) >= c_bound[0]
    )
    MnM.add_constraint(
        MnM.sum(protein[k] * x[i, t, k] for i in range(2) for t in range(5) for k in range(K)) >= p_bound[0]
    )
    MnM.add_constraint(
        MnM.sum(fat[k] * x[i, t, k] for i in range(2) for t in range(5) for k in range(K)) >= f_bound[0]
    )
    MnM.add_constraint(
        MnM.sum(sodium[k] * x[i, t, k] for i in range(2) for t in range(5) for k in range(K)) >= s_bound[0]
    )

    # nutrition upper bound
    MnM.add_constraint(
        MnM.sum(calories[k] * x[i, t, k] for i in range(2) for t in range(5) for k in range(K)) <= c_bound[1]
    )
    MnM.add_constraint(
        MnM.sum(protein[k] * x[i, t, k] for i in range(2) for t in range(5) for k in range(K)) <= p_bound[1]
    )
    MnM.add_constraint(
        MnM.sum(fat[k] * x[i, t, k] for i in range(2) for t in range(5) for k in range(K)) <= f_bound[1]
    )
    MnM.add_constraint(
        MnM.sum(sodium[k] * x[i, t, k] for i in range(2) for t in range(5) for k in range(K)) <= s_bound[1]
    )

    # budget constraint
    MnM.add_constraint(
        MnM.sum(price[k] * x[i, t, k] for i in range(2) for t in range(5) for k in range(K)) <= B
    )

    # schedule time inequalities
    MnM.add_constraint(
        MnM.sum(tau[k] * (x[0, t, k] - x[1, t, k]) for t in range(5) for k in range(K)) <= w
    )
    MnM.add_constraint(
        MnM.sum(tau[k] * (x[0, t, k] - x[1, t, k]) for t in range(5) for k in range(K)) >= -w
    )

    # schedule date constraint
    for i in range(2):
        for t in range(5):
            MnM.add_constraint(MnM.sum(x[i, t, k] for k in range(K)) <= T[i][t])

    MnM.maximize(
        MnM.sum((rating[0][k] + rating[1][k]) * x[i, t, k] for i in range(2) for t in range(5) for k in
                range(K)) - alpha * w
    )
    MnMs = MnM.solve()
    return tidy_data(recipe_list, name_list, MnMs.as_dict(x))


"""
tidy_data:
input:
1. recipe_list: the list of recipe(list of string)
2. name_list: the list of user name(list of string)
3. result of optimization(dictionary)
Output:
{
    'Monday': ['A', 'recipe A'],
    'Tuesday': ['B', 'recipe B'],
    'Wednesday': ['B', 'recipe C'],
    'Thursday': ['A', 'recipe B'],
    'Friday': ['A', 'recipe D'],
}
"""


def tidy_data(recipe_list, name_list, result):
    res = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }
    for key in result.keys():
        if key == 'w':
            continue
        else:
            key_list = key.split('_')
            name = name_list[int(key_list[1])]
            recipe = recipe_list[int(key_list[3])]
            if key_list[2] == '0':
                res['Monday'] = [name, recipe]
            elif key_list[2] == '1':
                res['Tuesday'] = [name, recipe]
            elif key_list[2] == '2':
                res['Wednesday'] = [name, recipe]
            elif key_list[2] == '3':
                res['Thursday'] = [name, recipe]
            elif key_list[2] == '4':
                res['Friday'] = [name, recipe]
    return res

from docplex.mp.model import Model
import backend.meal_problem.collaborative_filtering as cf

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

    calories = [
        526.0, 699.0, 578.0, 530.0, 502.0, 329.0, 703.0, 429.0, 1010.0, 139.0, 657.0, 346.0, 620.0, 467.0,
        599.0, 2887.0, 486.0, 1448.0, 460.0, 847.0, 351.0, 612.0, 549.0, 577.0, 1141.0, 885.0, 820.0, 572.0,
        364.0, 539.0, 2013.0, 791.0, 458.0, 730.0, 1032.0, 637.0, 810.0, 544.0, 711.0, 257.0, 892.0, 828.0,
        1062.0, 652.0, 523.0, 756.0, 355.0, 631.0, 513.0, 820.0, 719.0, 586.0, 656.0, 733.0, 816.0, 707.0,
        673.0, 481.0, 441.0, 503.0, 723.0, 428.0, 245.0, 591.0, 688.0, 563.0, 157.0, 612.0, 681.0, 588.0,
        1033.0, 725.0, 959.0, 194.0, 264.0, 137.0, 470.0, 393.0, 162.0, 256.0, 640.0, 492.0, 560.0, 461.0,
        564.0, 835.0, 744.0, 737.0, 318.0, 534.0, 3597.0, 403.0, 497.0, 616.0, 437.0, 1040.0, 890.0, 219.0,
        1051.0, 263.0, 123.0, 708.0, 581.0, 691.0, 606.0, 375.0, 388.0, 233.0, 526.0, 656.0, 188.0, 420.0,
        284.0, 467.0, 165.0
    ]
    protein = [
        43.0, 50.0, 34.0, 13.0, 12.0, 20.0, 23.0, 6.0, 12.0, 3.0, 41.0, 3.0, 61.0, 10.0, 32.0, 63.0, 38.0, 56.0,
        15.0, 46.0, 21.0, 25.0, 42.0, 23.0, 34.0, 56.0, 28.0, 53.0, 6.0, 37.0, 312.0, 30.0, 31.0, 58.0, 51.0,
        21.0, 40.0, 24.0, 21.0, 10.0, 37.0, 25.0, 48.0, 22.0, 43.0, 51.0, 5.0, 29.0, 20.0, 45.0, 31.0, 28.0,
        50.0, 23.0, 39.0, 35.0, 38.0, 8.0, 39.0, 29.0, 30.0, 5.0, 8.0, 10.0, 48.0, 40.0, 4.0, 25.0, 61.0, 48.0,
        44.0, 46.0, 1.0, 2.0, 7.0, 13.0, 8.0, 13.0, 8.0, 3.0, 39.0, 8.0, 35.0, 21.0, 55.0, 57.0, 45.0, 52.0,
        30.0, 45.0, 33.0, 8.0, 29.0, 13.0, 13.0, 20.0, 28.0, 9.0, 63.0, 4.0, 1.0, 20.0, 36.0, 46.0, 27.0, 9.0,
        8.0, 7.0, 13.0, 22.0, 15.0, 35.0, 8.0, 21.0, 2.0
    ]
    fat = [
        23.0, 35.0, 23.0, 42.0, 31.0, 26.0, 29.0, 32.0, 85.0, 9.0, 46.0, 19.0, 34.0, 9.0, 17.0, 205.0, 34.0, 102.0,
        13.0, 62.0, 20.0, 27.0, 36.0, 38.0, 77.0, 28.0, 47.0, 10.0, 11.0, 24.0, 64.0, 34.0, 21.0, 46.0, 67.0, 37.0,
        53.0, 28.0, 48.0, 21.0, 38.0, 44.0, 60.0, 24.0, 21.0, 32.0, 18.0, 40.0, 20.0, 56.0, 52.0, 47.0, 34.0, 34.0,
        52.0, 61.0, 29.0, 36.0, 18.0, 34.0, 36.0, 21.0, 13.0, 56.0, 25.0, 23.0, 11.0, 35.0, 43.0, 39.0, 53.0, 34.0,
        0.0, 11.0, 16.0, 8.0, 45.0, 19.0, 5.0, 15.0, 49.0, 28.0, 37.0, 23.0, 35.0, 52.0, 51.0, 50.0, 8.0, 14.0,
        223.0, 25.0, 30.0, 37.0, 28.0, 75.0, 60.0, 10.0, 64.0, 18.0, 6.0, 41.0, 36.0, 34.0, 15.0, 16.0, 19.0, 17.0,
        23.0, 36.0, 5.0, 20.0, 21.0, 36.0, 14.0
    ]
    sodium = [
        715.0, 1189.0, 1151.0, 627.0, 1055.0, 327.0, 1144.0, 316.0, 273.0, 539.0, 999.0, 220.0, 1289.0, 1833.0,
        968.0, 2691.0, 571.0, 784.0, 503.0, 953.0, 716.0, 765.0, 760.0, 839.0, 2287.0, 1257.0, 713.0, 1592.0,
        183.0, 758.0, 12856.0, 721.0, 1825.0, 1231.0, 1592.0, 567.0, 1372.0, 840.0, 1104.0, 659.0, 982.0, 940.0,
        2000.0, 1364.0, 1125.0, 1041.0, 243.0, 1512.0, 617.0, 977.0, 1600.0, 816.0, 1277.0, 1509.0, 1015.0, 598.0,
        1089.0, 496.0, 1134.0, 1574.0, 806.0, 300.0, 571.0, 496.0, 1668.0, 813.0, 226.0, 906.0, 1198.0, 745.0,
        3495.0, 801.0, 13.0, 110.0, 513.0, 247.0, 289.0, 877.0, 539.0, 113.0, 573.0, 413.0, 482.0, 407.0, 852.0,
        1813.0, 1099.0, 708.0, 807.0, 968.0, 1869.0, 419.0, 1177.0, 935.0, 667.0, 1047.0, 1283.0, 858.0, 1212.0,
        50.0, 266.0, 733.0, 1044.0, 779.0, 1365.0, 794.0, 301.0, 363.0, 1262.0, 1089.0, 483.0, 843.0, 619.0,
        1050.0, 373.0
    ]
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

import numpy as np
from sklearn.linear_model import LinearRegression
import math


def player_predictor(a1, decimal):
    first_index = (len(a1) - (math.floor(len(a1) * decimal)))
    res_size = a1[first_index:]

    y = np.array(res_size)
    x = np.arange(len(res_size)).reshape((-1, 1))

    model = LinearRegression().fit(x, y)

    x_new = np.array([len(res_size), len(res_size) + 1]).reshape((-1, 1))

    y_new = model.predict(x_new)

    res = [round(y_new[0], 3), round(y_new[1], 3)]

    for i in range(len(res)):
        if res[i] < 0:
            res[i] = 0
    
    return res

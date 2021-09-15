import numpy as np
from sklearn.linear_model import LinearRegression


def predict(a1):

    y = np.array(a1)
    x = np.arange(len(a1)).reshape((-1, 1))

    model = LinearRegression().fit(x, y)

    x_new = np.array([len(a1), len(a1)+1]).reshape((-1, 1))


    y_new = model.predict(x_new)
    print(y_new)





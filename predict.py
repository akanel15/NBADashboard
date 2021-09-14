import numpy as np
from sklearn.linear_model import LinearRegression



def predict(a1):

    y = np.array(a1)
    x = np.arange(len(a1)).reshape((-1, 1))
    print(y)

    model = LinearRegression().fit(x, y)

    x_new = np.array([8, 9]).reshape((-1, 1))
    print(x_new)


    y_new = model.predict(x_new)
    print(y_new)

pts =[32.57692307692308, 26.88235294117647, 30.378048780487806, 29.646341463414632, 28.74390243902439, 22.916666666666668, 20]

predict(pts)



import unittest

from predict import player_predictor


class TestPredict(unittest.TestCase):
    def test_predict_lebron_james(self):
        self.assertEqual(player_predictor(
            [20.936708860759495, 27.1875, 31.367088607594937, 27.333333333333332, 30.0, 28.444444444444443,
             29.710526315789473, 26.72151898734177, 27.14516129032258, 26.789473684210527, 27.12987012987013,
             25.26086956521739, 25.263157894736842, 26.405405405405407, 27.451219512195124, 27.363636363636363,
             25.34328358208955, 25.022222222222222], 0.3), [24.9, 24.4])

    def test_predict_stephen_curry(self):
        self.assertEqual(player_predictor(
            [17.4875, 18.554054054054053, 14.73076923076923, 22.897435897435898, 24.012820512820515, 23.75,
             30.063291139240505, 25.303797468354432, 26.392156862745097, 27.26086956521739, 20.8, 31.984126984126984],
            0.3), [31.4, 33.8])

    def test_predict_anthony_davis(self):
        self.assertEqual(player_predictor(
            [13.546875, 20.80597014925373, 24.352941176470587, 24.278688524590162,27.986666666666668,
             28.133333333333333, 25.928571428571427, 26.096774193548388, 21.833333333333332], 0.3), [17.6, 13.3])


if __name__ == "__main__":
    unittest.main()

import unittest

from predict import player_predictor
from rating_calc import defensive_rating_calc, offensive_rating_calc

class TestPredict(unittest.TestCase):
    def test_predict_lebron_james_pts(self):
        self.assertEqual(player_predictor(
            [20.936708860759495, 27.1875, 31.367088607594937, 27.333333333333332, 30.0, 28.444444444444443,
             29.710526315789473, 26.72151898734177, 27.14516129032258, 26.789473684210527, 27.12987012987013,
             25.26086956521739, 25.263157894736842, 26.405405405405407, 27.451219512195124, 27.363636363636363,
             25.34328358208955, 25.022222222222222], 0.3), [24.855, 24.367])

    def test_predict_stephen_curry_pts(self):
        self.assertEqual(player_predictor(
            [17.4875, 18.554054054054053, 14.73076923076923, 22.897435897435898, 24.012820512820515, 23.75,
             30.063291139240505, 25.303797468354432, 26.392156862745097, 27.26086956521739, 20.8, 31.984126984126984],
            0.3), [31.405, 33.767])

    def test_predict_anthony_davis_pts(self):
        self.assertEqual(player_predictor(
            [13.546875, 20.80597014925373, 24.352941176470587, 24.278688524590162,27.986666666666668,
             28.133333333333333, 25.928571428571427, 26.096774193548388, 21.833333333333332], 0.3), [17.57, 13.306])

    def test_predict_lebron_james_reb(self):
        self.assertEqual(player_predictor(
            [5.468354430379747, 7.35, 7.037974683544304, 6.743589743589744, 7.8933333333333335, 7.567901234567901, 
             7.2894736842105265, 7.468354430379747, 7.935483870967742, 8.026315789473685, 6.922077922077922, 
             6.028985507246377, 7.434210526315789, 8.635135135135135, 8.646341463414634, 8.454545454545455, 
             7.835820895522388, 7.688888888888889, 7.441, 7.171], 0.3), [6.817, 6.515])

    def test_defensive_rating_calc_stl(self):
        self.assertEqual(defensive_rating_calc(1.4, 1.2), 98)
        self.assertEqual(defensive_rating_calc(1.2, 1.2), 96)

    def test_defensive_rating_calc_blk(self):
        self.assertEqual(defensive_rating_calc(0.8, 1.4), 90)
        self.assertEqual(defensive_rating_calc(0.8, 1.2), 88)

    def test_offensive_rating_calc(self):
        self.assertEqual(offensive_rating_calc(29, 5, 5, 0.4), 92)
        self.assertEqual(offensive_rating_calc(27, 5, 5, 0.4), 91)
        self.assertEqual(offensive_rating_calc(29, 9, 5, 0.4), 95)
        self.assertEqual(offensive_rating_calc(29, 7, 5, 0.4), 94)
        self.assertEqual(offensive_rating_calc(29, 5, 12, 0.4), 96)
        self.assertEqual(offensive_rating_calc(29, 5, 10, 0.4), 96)
        self.assertEqual(offensive_rating_calc(29, 5, 11, 0.6), 97)
        self.assertEqual(offensive_rating_calc(29, 5, 11, 0.4), 96)

if __name__ == "__main__":
    unittest.main()

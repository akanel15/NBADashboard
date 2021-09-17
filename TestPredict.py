import unittest

from predict import player_predictor


class TestPredict(unittest.TestCase):
    def test_predict(self):
        self.assertAlmostEqual(player_predictor(
            [20.936708860759495, 27.1875, 31.367088607594937, 27.333333333333332, 30.0, 28.444444444444443,
             29.710526315789473, 26.72151898734177, 27.14516129032258, 26.789473684210527, 27.12987012987013,
             25.26086956521739, 25.263157894736842, 26.405405405405407, 27.451219512195124, 27.363636363636363,
             25.34328358208955, 25.022222222222222], 0.3), [24.85486272816815, 24.367432498520955])


if __name__ == "__main__":
    unittest.main()

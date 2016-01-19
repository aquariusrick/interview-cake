import unittest
from problems.ex02 import get_product_of_all_ints_except_at_index


class TestExercise02(unittest.TestCase):
    def test_success(self):
        assertions = [
            ([1, 7, 3, 4], [84, 12, 28, 21]),
            ([2, 7, 3, 4], [7*3*4, 2*3*4, 2*7*4, 2*7*3]),
            ([2, 0, 3, 4], [0*3*4, 2*3*4, 2*0*4, 2*0*3]),
            ([1, 2, 6, 5, 9], [540, 270, 90, 108, 60]),
        ]
        for test_data, expected in assertions:
            result = get_product_of_all_ints_except_at_index(test_data)
            self.assertEqual(result, expected)


"""
1, 7, 3, 4

[7, 1]

[
[7*3, 1*3, 1*7]
[21, 3, 7]

[7*3*4, 1*3*4, 7*1*4, 7*3*1*3*7*1]


"""
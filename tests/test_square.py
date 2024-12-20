import unittest
from square import area, perimeter


class TestAreaSquare(unittest.TestCase):

    def test_area(self):
        a = 5
        expected_area = a * a
        result = area(a)
        self.assertAlmostEqual(result, expected_area)

    def test_area_invalid_side(self):
        invalid_side = [0, -1, -100]
        for side in invalid_side:
            with self.subTest(side=side):
                with self.assertRaises(ValueError):
                    area(side)


class TestPerimeterSquare(unittest.TestCase):

    def test_perimetr(self):
        a = 7
        expected_perimetr = 4 * a
        result = perimeter(a)
        self.assertAlmostEqual(result, expected_perimetr)

    def test_perimeter_invalid_side(self):
        invalid_side = [0, -1, -100]
        for side in invalid_side:
            with self.subTest(side=side):
                with self.assertRaises(ValueError):
                    perimeter(side)


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()

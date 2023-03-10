import unittest
import main


class ValidityTestCase(unittest.TestCase):
    def test_isbn_ten(self):
        self.assertEqual(main.isbn10("0330301624"), True)

    def test_isbn_thirteen(self):
        self.assertEqual(main.isbn13("9780316066525"), True)

    def test_convert(self):
        self.assertEqual(main.convertTo13("0316066524"), "9780316066525")


if __name__ == '__main__':
    unittest.main()

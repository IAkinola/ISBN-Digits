import unittest
import main


class ValidityTestCase(unittest.TestCase):
    def test_isbn_ten(self):
        result = main.isbn10("0330301624")
        self.assertEqual(result, True)

    def test_isbn_thirteen(self):
        result = main.isbn13("9780316066525")
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()

import unittest

from NextDate1 import NextDate1


class TestNextDate1(unittest.TestCase):
    date = NextDate1()
    print("Enter today's date")
    month = input("Enter MM: ")
    day = input("Enter DD: ")
    year = input("Enter YYYY: ")
    date.Date(month, day, year)

if __name__ == "__main__":
    unittest.main()

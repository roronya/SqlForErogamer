import sqlforerogamer
import unittest

class TestSqlforerogamer(unittest.TestCase):
    def test_tables(self):
        print(sqlforerogamer.tables())

if __name__ == '__main__':
    unittest.main()

import unittest
import sqlforerogamer
import pandas

class TestSqlforerogamer(unittest.TestCase):
    def test_read(self):
        sql = 'select * from brandlist limit 10'
        result = sqlforerogamer.read(sql)
        self.assertIsInstance(result, pandas.DataFrame)
        sql = 'select * from unexistingtable'
        with self.assertRaises(ValueError):
            sqlforerogamer.read(sql)

    def test_tables(self):
        result = sqlforerogamer.tables()
        self.assertIsInstance(result, pandas.DataFrame)


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""test_db_storage module"""
import pep8
import unittest
import MySQLdb
import os
from os import getenv
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestDBStorage(unittest.TestCase):
    '''Test class for db_storage'''

    @classmethod
    def setUpClass(cls):
        """setup method"""
        cls.User = getenv("HBNB_MYYSQL_USER")
        cls.Passwd = getenv("HBNB_MYSQL_PWD")
        cls.Db = getenv("HBNB_MYSQL_DB")
        cls.Host = getenv("HBNB_MYSQL_HOST")
        cls.db = MySqldb.connect(host=self.Host, user=self.User,
                                 passwd=self.Passwd, db=self.Db,
                                 charset="utf8")
        cls.query = self.db.cursor()
        cls.storage = DBStorage()
        cls.storage.reload()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_pep8_DBStorage(self):
        """pep8 method"""
        style = pep8.StyleGuide(quiet=True)
        checker = style.check_files
        (['models/engine/db_storage.py'])
        self.assertEqual(style.total_errors, 0,
                         "errors where found")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_read_tables(self):
        """method for checking the exisiting tables"""
        self.query.execute("SHOW TABLES")
        result = self.query.fetchall()
        self.assertEqual(len(result), 7)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_no_element_user(self):
        """checks for elements in users table"""
        self.query.execute("SELECT * FROM users")
        result = self.query.fetchall()
        self.assertEqual(len(result), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_no_element_cities(self):
        """checks for elements in table cities"""
        self.query.execute("SELECT * FROM cities")
        result = self.query.fetchall()
        self.assertEqual(len(result), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add(self):
        """Test same size between storage() and existing db"""
        self.query.execute("SELECT * FROM states")
        result = self.query.fetchall()
        self.assertEqual(len(result), 0)
        state = State(name="California")
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT * FROM states")
        result = self.query.fetchall()
        self.assertEqual(len(result), 1)

    @classmethod
    def tearDownClass(cls):
        """clean up method"""
        cls.query.close()
        cls.db.close()


if __name__ == "__main__":
    unittest.main()

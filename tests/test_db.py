# -*- coding: utf-8 -*-

import unittest
from peewee import SqliteDatabase
import unittest
from ..app import app  #
from ..db import ProductModel, create_product, get_product_by_id, update_product, delete_product

# Решта тестів залишаються без змін


class TestDBFunctions(unittest.TestCase):
    def setUp(self):
        self.test_db = SqliteDatabase(':memory:')  # In-memory database for testing
        ProductModel._meta.database = self.test_db
        self.test_db.connect()
        self.test_db.create_tables([ProductModel])

        self.product = create_product('Test Product', 50)

    def tearDown(self):
        self.test_db.close()



if __name__ == '__main__':
    unittest.main()

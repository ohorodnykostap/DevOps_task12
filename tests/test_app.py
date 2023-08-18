import unittest
from app import app
from peewee import SqliteDatabase
from playhouse.test_utils import test_database
from db import ProductModel, create_product

# Use an in-memory SQLite database for testing
test_db = SqliteDatabase(":memory:")

class TestProductAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db_context = test_database(test_db, [ProductModel])
        self.db_context.__enter__()
        test_db.create_tables([ProductModel])
    
 
if __name__ == "__main__":
    unittest.main()

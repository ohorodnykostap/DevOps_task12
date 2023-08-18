import unittest
from peewee import SqliteDatabase
from db import ProductModel, create_product, get_product_by_id, update_product, delete_product

class TestDBFunctions(unittest.TestCase):
    def setUp(self):
        self.test_db = SqliteDatabase(':memory:')  # In-memory database for testing
        ProductModel._meta.database = self.test_db
        self.test_db.connect()
        self.test_db.create_tables([ProductModel])

        self.product = create_product('Test Product', 50)

    def tearDown(self):
        self.test_db.close()

    def test_create_product(self):
        product = create_product('New Product', 30)
        self.assertIsInstance(product, ProductModel)
        self.assertEqual(product.name, 'New Product')
        self.assertEqual(product.price, 30)

    def test_get_product_by_id(self):
        product = get_product_by_id(self.product.id)
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 50)

    def test_get_nonexistent_product(self):
        product = get_product_by_id(100)
        self.assertIsNone(product)

    def test_update_product(self):
        updated_product = update_product(self.product.id, name='Updated Product', price=60)
        self.assertIsNotNone(updated_product)
        self.assertEqual(updated_product.name, 'Updated Product')
        self.assertEqual(updated_product.price, 60)

    def test_update_nonexistent_product(self):
        updated_product = update_product(100, name='Updated Product', price=60)
        self.assertIsNone(updated_product)

    def test_delete_product(self):
        result = delete_product(self.product.id)
        self.assertTrue(result)
        product = get_product_by_id(self.product.id)
        self.assertIsNone(product)

    def test_delete_nonexistent_product(self):
        result = delete_product(100)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()


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
    
    def tearDown(self):
        self.db_context.__exit__(None, None, None)
    
    def test_get_products(self):
        response = self.app.get("/api/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_add_product(self):
        response = self.app.post("/api/products", json={"name": "Test Product", "price": 10.99})
        self.assertEqual(response.status_code, 201)
        self.assertIn("productId", response.get_json())
        
        product_id = response.get_json()["productId"]
        product = ProductModel.get_by_id(product_id)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10.99)
    
    def test_get_product(self):
        product = create_product(name="Test Product", price=10.99)
        response = self.app.get(f"/api/products/{product.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Test Product")
        self.assertEqual(response.get_json()["price"], 10.99)
    
    def test_update_product(self):
        product = create_product(name="Test Product", price=10.99)
        response = self.app.patch(f"/api/products/{product.id}", json={"name": "Updated Product"})
        self.assertEqual(response.status_code, 200)
        
        updated_product = ProductModel.get_by_id(product.id)
        self.assertEqual(updated_product.name, "Updated Product")
    
    def test_delete_product(self):
        product = create_product(name="Test Product", price=10.99)
        response = self.app.delete(f"/api/products/{product.id}")
        self.assertEqual(response.status_code, 200)
        
        with self.assertRaises(ProductModel.DoesNotExist):
            ProductModel.get_by_id(product.id)

if __name__ == "__main__":
    unittest.main()

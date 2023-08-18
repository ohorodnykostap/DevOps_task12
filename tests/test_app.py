import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_products(self):
        response = self.app.get('/api/products')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 5)  # Assuming there are 5 default products

    def test_get_product_by_id(self):
        response = self.app.get('/api/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], 'Sugar')
        self.assertEqual(response.json['price'], 32)

    def test_get_nonexistent_product(self):
        response = self.app.get('/api/products/10')
        self.assertEqual(response.status_code, 404)

    def test_create_product(self):
        data = {'name': 'Tea', 'price': 15}
        response = self.app.post('/api/products', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('productId', response.json)

    def test_update_product(self):
        data = {'name': 'Updated Product', 'price': 25}
        response = self.app.patch('/api/products/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_update_nonexistent_product(self):
        data = {'name': 'Updated Product', 'price': 25}
        response = self.app.patch('/api/products/10', json=data)
        self.assertEqual(response.status_code, 404)

    def test_delete_product(self):
        response = self.app.delete('/api/products/1')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()


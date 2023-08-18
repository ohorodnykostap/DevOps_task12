# tests/test_db.py

import pytest
from db import db, ProductModel, create_product

@pytest.fixture(scope="module")
def setup_database():
    db.connect()
    db.create_tables([ProductModel])
    yield
    db.drop_tables([ProductModel])
    db.close()

def test_create_product(setup_database):
    product = create_product("Test Product", 10)
    assert product.name == "Test Product"
    assert product.price == 10

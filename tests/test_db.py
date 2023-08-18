import pytest
from peewee import OperationalError, SqliteDatabase
from db import *

@pytest.fixture(scope='module')
def test_db():
    db.connect()
    db.create_tables([ProductModel])

    yield db

    db.drop_tables([ProductModel])
    db.close()

def test_create_product(test_db):
    product = create_product("Test Product", 10)
    assert product is not None
    assert product.id is not None

def test_get_product_by_id(test_db):
    product = create_product("Test Product", 10)
    retrieved_product = get_product_by_id(product.id)
    assert retrieved_product is not None
    assert retrieved_product.name == "Test Product"

def test_update_product(test_db):
    product = create_product("Test Product", 10)
    updated_product = update_product(product.id, price=15)
    assert updated_product is not None
    assert updated_product.price == 15

def test_delete_product(test_db):
    product = create_product("Test Product", 10)
    delete_product(product.id)
    with pytest.raises(ProductModel.DoesNotExist):
        get_product_by_id(product.id)


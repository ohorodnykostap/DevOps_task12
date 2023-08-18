import pytest
from db import db, ProductModel, create_product, get_product_by_id, update_product, delete_product
from peewee import OperationalError, DoesNotExist


@pytest.fixture(scope="function")
def test_db():
    db.connect()
    db.create_tables([ProductModel])
    yield
    db.drop_tables([ProductModel])
    db.close()


def test_create_product(test_db):
    product = create_product("Test Product", 10)
    assert product.id is not None


def test_get_product_by_id(test_db):
    product = create_product("Test Product", 10)
    retrieved_product = get_product_by_id(product.id)
    assert retrieved_product is not None


def test_update_product(test_db):
    product = create_product("Test Product", 10)
    updated_product = update_product(product.id, name="Updated Product")
    assert updated_product is not None
    assert updated_product.name == "Updated Product"


def test_delete_product(test_db):
    product = create_product("Test Product", 10)
    result = delete_product(product.id)
    assert result is True
    deleted_product = get_product_by_id(product.id)
    assert deleted_product is None


def test_get_product_by_id_nonexistent(test_db):
    retrieved_product = get_product_by_id(999)
    assert retrieved_product is None


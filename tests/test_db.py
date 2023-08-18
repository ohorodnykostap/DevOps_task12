import pytest
from peewee import OperationalError, SqliteDatabase
from db import *

# Решта вашого коду для тестів...


@pytest.fixture(scope="function", autouse=True)
def test_db():
    db = SqliteDatabase(':memory:')  # Використовуємо пам'ять як базу даних для тестів
    ProductModel._meta.database = db
    db.connect()
    yield
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


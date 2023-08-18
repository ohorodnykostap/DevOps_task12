from db import create_product, get_product_by_id

def test_create_product():
    product = create_product("Test Product", 10)
    assert product.name == "Test Product"
    assert product.price == 10

def test_get_product_by_id():
    product = create_product("Test Product", 10)
    retrieved_product = get_product_by_id(product.id)
    assert retrieved_product.name == "Test Product"
    assert retrieved_product.price == 10

from app.demo import ShoppingCart
import pytest

@pytest.fixture
def cart():
  return ShoppingCart()

@pytest.mark.skip("")
def test_add(cart):
  cart.add_item('apple',2)
  assert cart.get_item_count("apple") == 2
  assert cart.get_total_items() == 2

def test_remove_item(cart):
  cart.add_item('apple',3)
  cart.remove_item('apple',1)
  assert cart.get_item_count("apple") == 2
  assert cart.get_total_items() == 2

def test_get_cart_items(cart):
  cart.add_item('apple',3)
  cart.add_item('orange',2)
  items = cart.get_cart_items() 
  assert "apple" in items
  assert "orange" in items

def test_clear_cart(cart):
  cart.add_item('apple',3)
  cart.add_item('orange',2)
  cart.clear_cart()
  assert cart.get_total_items() == 0
  assert cart.get_cart_items() == []



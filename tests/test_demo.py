from app.demo import add,sub,mul,div,discount_season
import pytest

@pytest.mark.skip("Skipping for some reason")
def test_add():
  assert add(1, 2) == 3

def test_sub():
  assert sub(3,2) == 1

@pytest.mark.skipif(discount_season(),reason="Skip if it's discount season")
def test_mul():
  assert mul(2,2) == 4

def test_div():
  assert div(4,2) == 2

  # Case for asserting exception
  with pytest.raises(ValueError):
    div(4,0)
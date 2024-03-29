from greet import greet
import pytest

def test_greet():
  assert greet('iBOTS') == "Hello, iBOTS!"
  assert greet('Sourav') == "Hello, Sourav!"
  assert greet('Yonatan') == "Hello, Yonatan!"
  assert greet('Yonatan') != "Hello, Sourav!"
  with pytest.raises(TypeError):
    assert greet(5)

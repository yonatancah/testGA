from greet import greet

def test_greet():
  assert greet('iBOTS') == "Hello, iBOTS!"
  assert greet('Sourav') == "Hello, Sourav!"
  assert greet('Yonatan') == "Hello, Yonatan!"

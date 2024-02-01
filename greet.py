def greet(name):
  if isinstance(name)==str:
    return f"Hello, {name}!"
  else:
    raise TypeError

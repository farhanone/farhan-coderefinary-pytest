import pytest
#@pytest.mark.add
#pytest -k add -v example.py 
def add(a, b):
    return a + b
def sub(a, b):
    return a - b

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    
def test_sub():
    assert sub(2, 3) == -1
    assert sub(3, 3) == 'spaceship'

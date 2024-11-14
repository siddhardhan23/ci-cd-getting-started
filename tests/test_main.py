from app.main import add

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert add(5, 2) == 3
    assert add(0, 0) == 0
    assert add(4, 4) == 0

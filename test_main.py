import main
import pytest

@pytest.mark.parametrize("x, y, expected", (
    (2, 3, 8),
    (0, 0, 2),
    (-1, 4, -2)
))

def test_bar(x, y, expected):
    assert main.foo(x, y) == expected
    

def test_bar():
    assert pytest.approx(main.foo(2, 3)) == 8
    assert pytest.approx(main.foo(0, 0)) == 2
    assert pytest.approx(main.foo(-1, 4)) == -2

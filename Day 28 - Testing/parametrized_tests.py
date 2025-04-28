import pytest
from calculator import multiply

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-4, 5, -20),
    (0, 100, 0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
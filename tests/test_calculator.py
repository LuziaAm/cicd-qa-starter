import pytest
from app.calculator import add, sub, mul, div

@pytest.mark.sanity
def test_add():
    assert add(2, 3) == 5

@pytest.mark.sanity
def test_sub():
    assert sub(10, 4) == 6

@pytest.mark.full
def test_mul():
    assert mul(3, 5) == 15

@pytest.mark.full
def test_div():
    assert div(10, 2) == 5

@pytest.mark.full
def test_div_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)

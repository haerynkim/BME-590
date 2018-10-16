import pytest
from add import add_ints

def test_add_ints_bad_type():
    with pytest.raises(TypeError):
        add_ints(2,2)

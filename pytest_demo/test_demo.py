import pytest


def add(a, b):
    return a + b


class TestAdd:
    @pytest.mark.skip
    def test_int(self):
        result = add(1, 2)
        assert result == 3

    def test_float(self):
        result = add(1.0, 2.0)
        assert result == 3.0

    def test_str(self):
        result = add("1", "2")
        assert result == "32"

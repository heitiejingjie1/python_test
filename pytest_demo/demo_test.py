import pytest
from data_input import data_f


def add(a, b):
    return a + b


class TestAdd:
    @pytest.mark.skip
    def test_int(self):
        result = add(1, 2)
        assert result == 3

    @pytest.mark.web
    def test_float(self):
        result = add(1.0, 2.0)
        assert result == 3.0

    @pytest.mark.login
    def test_str(self):
        result = add("1", "2")
        assert result == "12"

    @pytest.mark.skipif(1 == 1, reason="不运行")
    def test_diff_str(self):
        a = "aaaaa"
        b = "aaaabc"

        assert a == b

    @pytest.mark.ddt
    @pytest.mark.parametrize("a,b,c", data_f("data.csv"))
    def test_para(self, a, b, c):
        result = add(int(a), int(b))

        assert result == int(c)

    @pytest.mark.xfail
    def test_int2(self):
        result = add(3, 8)

        assert result == 10

    @pytest.mark.xfail
    def test_int3(self):
        result = add(3, 8)

        assert result != 10


class TestDemo:
    def test_func(self):
        pass

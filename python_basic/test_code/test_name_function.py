from name_function import get_formatted_name


def test_first_last_name():
    """能处理像Yin Hao这样的姓名吗"""
    formatted_name = get_formatted_name("yin", "hao")
    assert formatted_name == "Yin Hao"


def test_first_middle_last_name():
    """能处理像Yin De Hao这样的姓名吗"""
    formatted_name = get_formatted_name("yin", "hao", middle="de")
    assert formatted_name == "Yin De Hao"

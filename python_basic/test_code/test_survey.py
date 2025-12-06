from survey import AnonymousSurvey
import pytest


"""使用夹具"""


@pytest.fixture
def language_survey():
    """可供测试使用的AnonymousSurvey实例"""
    question = "你最喜欢的语言是什么？"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    language_survey.store_response("rust")
    assert "rust" in language_survey.responses


def test_store_three_response(language_survey):
    """测试三个答案被妥善地存储"""
    responses = ["rust", "cpp", "python"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

import pytest

from app.prompt_service import PromptService


def test_build_prompt_success():

    service = PromptService()

    result = service.build_prompt("Что такое Python?")

    assert result == "Ответь подробно на следующий запрос: Что такое Python?"


def test_build_prompt_empty():

    service = PromptService()

    with pytest.raises(ValueError):
        service.build_prompt("")
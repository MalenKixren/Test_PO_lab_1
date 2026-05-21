import pytest

from app.prompt_service import PromptService


# Проверка корректного формирования prompt
def test_build_prompt_success():

    service = PromptService()

    result = service.build_prompt("Что такое Python?")

    assert result == "Ответь подробно на следующий запрос: Что такое Python?"


# Проверка обработки пустой строки
def test_build_prompt_empty():

    service = PromptService()

    with pytest.raises(ValueError):
        service.build_prompt("")


# Проверка строки из пробелов
def test_build_prompt_spaces():

    service = PromptService()

    result = service.build_prompt("   ")

    assert "Ответь подробно" in result


# Проверка длинного текста
def test_build_prompt_long_text():

    service = PromptService()

    text = "Python " * 100

    result = service.build_prompt(text)

    assert text in result


# Проверка специальных символов
def test_build_prompt_special_characters():

    service = PromptService()

    result = service.build_prompt("@#$%^&*")

    assert "@#$%^&*" in result

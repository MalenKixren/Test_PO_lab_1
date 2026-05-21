import pytest

from app.ai_client import AIClient


# Проверка успешной обработки prompt
def test_send_request_success():

    client = AIClient()

    result = client.send_request("Привет")

    assert result == "Привет"


# Проверка пустого prompt
def test_send_request_empty():

    client = AIClient()

    with pytest.raises(ValueError):
        client.send_request("")


# Проверка длинного prompt
def test_send_request_long_prompt():

    client = AIClient()

    prompt = "TEST " * 200

    result = client.send_request(prompt)

    assert prompt in result


# Проверка unicode символов
def test_send_request_unicode():

    client = AIClient()

    result = client.send_request("こんにちは")

    assert "こんにちは" in result

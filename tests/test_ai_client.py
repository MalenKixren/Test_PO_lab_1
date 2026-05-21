import pytest

from app.ai_client import AIClient


def test_send_request_success():

    client = AIClient()

    result = client.send_request("Привет")

    assert result == "AI RESPONSE: Привет"


def test_send_request_empty():

    client = AIClient()

    with pytest.raises(ValueError):
        client.send_request("")
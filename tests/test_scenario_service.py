from unittest.mock import Mock

from app.scenario_service import ScenarioService


# Проверка полного сценария работы
def test_execute_scenario():

    prompt_service = Mock()
    ai_client = Mock()
    history_service = Mock()

    prompt_service.build_prompt.return_value = "MOCK PROMPT"

    ai_client.send_request.return_value = "MOCK RESPONSE"

    service = ScenarioService(
        prompt_service,
        ai_client,
        history_service
    )

    result = service.execute_scenario("Привет")

    assert result == "MOCK RESPONSE"


# Проверка вызова build_prompt
def test_prompt_service_called():

    prompt_service = Mock()
    ai_client = Mock()
    history_service = Mock()

    prompt_service.build_prompt.return_value = "PROMPT"

    ai_client.send_request.return_value = "RESPONSE"

    service = ScenarioService(
        prompt_service,
        ai_client,
        history_service
    )

    service.execute_scenario("TEST")

    prompt_service.build_prompt.assert_called_once_with("TEST")


# Проверка вызова AI клиента
def test_ai_client_called():

    prompt_service = Mock()
    ai_client = Mock()
    history_service = Mock()

    prompt_service.build_prompt.return_value = "PROMPT"

    ai_client.send_request.return_value = "RESPONSE"

    service = ScenarioService(
        prompt_service,
        ai_client,
        history_service
    )

    service.execute_scenario("TEST")

    ai_client.send_request.assert_called_once_with("PROMPT")


# Проверка сохранения истории
def test_history_service_called():

    prompt_service = Mock()
    ai_client = Mock()
    history_service = Mock()

    prompt_service.build_prompt.return_value = "PROMPT"

    ai_client.send_request.return_value = "RESPONSE"

    service = ScenarioService(
        prompt_service,
        ai_client,
        history_service
    )

    service.execute_scenario("TEST")

    history_service.save_record.assert_called_once_with(
        "TEST",
        "RESPONSE"
    )


# Проверка обработки длинного ввода
def test_execute_scenario_long_input():

    prompt_service = Mock()
    ai_client = Mock()
    history_service = Mock()

    long_input = "HELLO " * 100

    prompt_service.build_prompt.return_value = "PROMPT"

    ai_client.send_request.return_value = "RESPONSE"

    service = ScenarioService(
        prompt_service,
        ai_client,
        history_service
    )

    result = service.execute_scenario(long_input)

    assert result == "RESPONSE"

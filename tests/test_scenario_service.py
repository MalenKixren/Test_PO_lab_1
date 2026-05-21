from unittest.mock import Mock

from app.scenario_service import ScenarioService


def test_execute_scenario():

    # Создаем mock-объекты
    prompt_service = Mock()
    ai_client = Mock()
    history_service = Mock()

    # Настраиваем поведение mock
    prompt_service.build_prompt.return_value = "MOCK PROMPT"

    ai_client.send_request.return_value = "MOCK RESPONSE"

    # Создаем тестируемый объект
    service = ScenarioService(
        prompt_service,
        ai_client,
        history_service
    )

    result = service.execute_scenario("Привет")

    # Проверяем результат
    assert result == "MOCK RESPONSE"

    # Проверяем вызовы методов
    prompt_service.build_prompt.assert_called_once_with("Привет")

    ai_client.send_request.assert_called_once_with("MOCK PROMPT")

    history_service.save_record.assert_called_once_with(
        "Привет",
        "MOCK RESPONSE"
    )
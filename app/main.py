from app.prompt_service import PromptService
from app.ai_client import AIClient
from app.history_service import HistoryService
from app.scenario_service import ScenarioService


def main():

    prompt_service = PromptService()
    ai_client = AIClient()
    history_service = HistoryService()

    scenario_service = ScenarioService(
        prompt_service,
        ai_client,
        history_service
    )

    user_input = input("Введите запрос: ")

    response = scenario_service.execute_scenario(user_input)

    print("\nИтоговый сформированный промпт:")
    print(response)

    print("\nИстория:")
    print(history_service.get_history())


if __name__ == "__main__":
    main()

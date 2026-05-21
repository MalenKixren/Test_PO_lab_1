# Основной сервис сценария

from app.prompt_service import PromptService
from app.ai_client import AIClient
from app.history_service import HistoryService


class ScenarioService:

    def __init__(
            self,
            prompt_service: PromptService,
            ai_client: AIClient,
            history_service: HistoryService
    ):

        self.prompt_service = prompt_service
        self.ai_client = ai_client
        self.history_service = history_service

    def execute_scenario(self, user_input: str) -> str:
        """
        Выполняет полный сценарий:
        1. Формирует prompt
        2. Отправляет в AI
        3. Сохраняет историю
        """

        prompt = self.prompt_service.build_prompt(user_input)

        response = self.ai_client.send_request(prompt)

        self.history_service.save_record(user_input, response)

        return response
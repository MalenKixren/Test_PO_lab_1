# Сервис формирования prompt для языковой модели

class PromptService:

    def build_prompt(self, user_input: str) -> str:
        """
        Формирует prompt для языковой модели.
        """

        if not user_input:
            raise ValueError("Пустой запрос пользователя")

        return f"Ответь подробно на следующий запрос: {user_input}"

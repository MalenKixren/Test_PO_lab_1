# Имитация клиента языковой модели

class AIClient:

    def send_request(self, prompt: str) -> str:
        """
        Проверка наличия запроса и возврат 
        """

        if not prompt:
            raise ValueError("Prompt пуст")

        # Имитация ответа модели
        return f"AI RESPONSE: {prompt}"

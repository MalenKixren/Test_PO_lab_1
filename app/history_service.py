# Сервис хранения истории запросов

class HistoryService:

    def __init__(self):
        self.history = []

    def save_record(self, user_input: str, response: str):
        """
        Сохраняет запрос и ответ.
        """

        self.history.append({
            "request": user_input,
            "response": response
        })

    def get_history(self):
        """
        Возвращает историю.
        """

        return self.history